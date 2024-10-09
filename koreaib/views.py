from django.shortcuts import render
from rest_framework.response import Response

from .models import (
    MarketBondCode,
    MarketBondIssueInfo,
    MarketBondSearchInfo,
    MarketBondInquireAskingPrice,
    MarketBondAvgUnit,
    MarketBondInquireDailyItemChartPrice,
    MarketBondInquirePrice,
    MarketBondInquireCCNL,
    MarketBondInquireDailyPrice,
    SearchKeyword,
    NaverNews,
)

from .serializer import (
    MarketBondCodeSerializer,
    MarketBondIssueInfoSerializer,
    MarketBondSearchInfoSerializer,
    MarketBondInquireAskingPriceSerializer,
    MarketBondAvgUnitSerializer,
    MarketBondInquireDailyItemChartPriceSerializer,
    MarketBondInquirePriceSerializer,
    MarketBondInquireCCNLSerializer,
    MarketBondInquireDailyPriceSerializer,
    SearchKeywordSerializer,
    NaverNewsSerializer,
)

from koreaib.kib_api.collect_kis_data import CollectMarketBond

from rest_framework import viewsets, status
from rest_framework.decorators import action

from django.core.serializers import serialize
import json

from koreaib.news_api.get_news_data import GetNewsData


import pandas as pd
import urllib.request
import ssl
import zipfile
import os

from django.db import transaction

base_dir = os.getcwd()


class MarketBondCodeViewSet(viewsets.ModelViewSet):


    queryset = MarketBondCode.objects.all()
    serializer_class = MarketBondCodeSerializer

    @transaction.atomic
    def create_bulk_data(self, data):
        serializer = MarketBondCodeSerializer(data=data, many=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @transaction.atomic
    def create_bulk_data(self, validated_data):
        MarketBondCode.objects.bulk_create([
            MarketBondCode(**item) for item in validated_data
        ], batch_size=1000)
    def download_and_extract_file(self, url, output_dir, zip_filename, extracted_filename):
        # Download the file
        print(f"Downloading {zip_filename}...")
        ssl._create_default_https_context = ssl._create_unverified_context
        zip_filepath = os.path.join(output_dir, zip_filename)
        urllib.request.urlretrieve(url, zip_filepath)

        # Extract the file
        print(f"Extracting {zip_filename}...")
        with zipfile.ZipFile(zip_filepath, "r") as zip_ref:
            zip_ref.extractall(output_dir)

        return os.path.join(output_dir, extracted_filename)

    def get_bond_master_dataframe(self, file_path):
        print("Parsing the file...")
        with open(file_path, mode="r", encoding="cp949") as f:
            lines = f.readlines()

        data = []
        for row in lines:
            row = row.strip()
            bond_type = row[0:2].strip()
            bond_cls_code = row[2:4].strip()
            stnd_iscd = row[4:16].strip()
            rdmp_date = row[-8:].strip()
            pblc_date = row[-16:-8].strip()
            lstn_date = row[-24:-16].strip()
            bond_int_cls_code = row[-26:-24].strip()
            sname = row[16:-26].rstrip()  # 종목명을 뒤에서부터 추출하여 남은 부분

            data.append(
                [
                    bond_type,
                    bond_cls_code,
                    stnd_iscd,
                    sname,
                    bond_int_cls_code,
                    lstn_date,
                    pblc_date,
                    rdmp_date,
                ]
            )

        columns = [
            "유형",
            "채권분류코드",
            "표준코드",
            "종목명",
            "채권이자분류코드",
            "상장일",
            "발행일",
            "상환일",
        ]

        df = pd.DataFrame(data, columns=columns)
        unique_pairs = df[['표준코드', '종목명']].drop_duplicates().sort_values('표준코드')
        code_name_list = [{'code': row['표준코드'], 'name': row['종목명']} for _, row in unique_pairs.iterrows()]

        return code_name_list


    @action(detail=False, methods=["GET"])
    def batch(self, request, *args, **kwargs):
        self.base_dir = os.getcwd()
        self.url = "https://new.real.download.dws.co.kr/common/master/bond_code.mst.zip"
        self.zip_filename = "bond_code.zip"
        self.extracted_filename = "bond_code.mst"
        self.file_path = self.download_and_extract_file(self.url, base_dir, self.zip_filename, self.extracted_filename)
        code_name_list = self.get_bond_master_dataframe(self.file_path)
        serializer = MarketBondCodeSerializer(data=code_name_list, many=True)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # self.create_bulk_data(code_name_list)
        return Response('not ok', status=status.HTTP_304_NOT_MODIFIED)


# Create your views here.
class MarketBondBaseViewSet(viewsets.ReadOnlyModelViewSet):
    def get_bond_code(self, code):
        if not code:
            return None, Response(
                {"error": "code is missing"}, status=status.HTTP_400_BAD_REQUEST
            )

        bond_code = MarketBondCode.objects.filter(code=code).first()
        if not bond_code:
            serializer = MarketBondCodeSerializer(data={"code": code})
            if serializer.is_valid():
                serializer.save()
            else:
                return None, Response(
                    {"error": "Failed to retrieve or create market bond code"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        bond_code = MarketBondCode.objects.filter(code=code).first()
        return bond_code, None

    def collect_and_get_info(self, code, bond_code, model, collect_method):
        info = model.objects.filter(code=bond_code).first()
        if not info:
            collector = CollectMarketBond(code, bond_code)
            getattr(collector, collect_method)()
            info = model.objects.filter(code=bond_code).first()
        return info

    def collect_and_get_multiple_info(self, code, bond_code, model, collect_method):
        info = model.objects.filter(code=bond_code)
        if not info:
            collector = CollectMarketBond(code, bond_code)
            getattr(collector, collect_method)()
            info = model.objects.filter(code=bond_code)
        return info

    def handle_response(self, instance, serializer_class):
        if instance:
            serializer = serializer_class(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Failed to retrieve or create info"},
                status=status.HTTP_404_NOT_FOUND,
            )


class MarketBondIssueInfoViewSet(MarketBondBaseViewSet):
    queryset = MarketBondIssueInfo.objects.all()
    serializer_class = MarketBondIssueInfoSerializer

    @action(detail=False, methods=["GET"])
    def market_bond_issue_info(self, request, *args, **kwargs):
        code = request.query_params.get("code")
        bond_code, error_response = self.get_bond_code(code)
        if error_response:
            return error_response
        try:
            issue_info = self.collect_and_get_info(
                code, bond_code, MarketBondIssueInfo, "store_market_bond_issue_info"
            )
            return self.handle_response(issue_info, self.serializer_class)
        except:
            return Response(
                {"error": "code is invalid"}, status=status.HTTP_400_BAD_REQUEST
            )


class MarketBondSearchInfoViewSet(MarketBondBaseViewSet):
    queryset = MarketBondSearchInfo.objects.all()
    serializer_class = MarketBondSearchInfoSerializer

    @action(detail=False, methods=["GET"])
    def market_bond_issue_info(self, request, *args, **kwargs):
        code = request.query_params.get("code")
        bond_code, error_response = self.get_bond_code(code)
        if error_response:
            return error_response
        try:
            issue_info = self.collect_and_get_info(
                code, bond_code, MarketBondSearchInfo, "store_market_search_bond_info"
            )
            return self.handle_response(issue_info, self.serializer_class)
        except:
            return Response(
                {"error": "code is invalid"}, status=status.HTTP_400_BAD_REQUEST
            )


class MarketBondInquireAskingPriceViewSet(MarketBondBaseViewSet):
    queryset = MarketBondInquireAskingPrice.objects.all()
    serializer_class = MarketBondInquireAskingPriceSerializer

    @action(detail=False, methods=["GET"])
    def market_bond_issue_info(self, request, *args, **kwargs):
        code = request.query_params.get("code")
        bond_code, error_response = self.get_bond_code(code)
        if error_response:
            return error_response
        try:
            issue_info = self.collect_and_get_info(
                code,
                bond_code,
                MarketBondInquireAskingPrice,
                "store_market_bond_inquire_asking_price",
            )
            return self.handle_response(issue_info, self.serializer_class)
        except:
            return Response(
                {"error": "code is invalid"}, status=status.HTTP_400_BAD_REQUEST
            )


class MarketBondAvgUnitViewSet(MarketBondBaseViewSet):
    queryset = MarketBondAvgUnit.objects.all()
    serializer_class = MarketBondAvgUnitSerializer

    @action(detail=False, methods=["GET"])
    def market_bond_issue_info(self, request, *args, **kwargs):
        code = request.query_params.get("code")
        bond_code, error_response = self.get_bond_code(code)
        if error_response:
            return error_response
        try:
            issue_info = self.collect_and_get_info(
                code, bond_code, MarketBondAvgUnit, "store_market_bond_avg_unit"
            )
            return self.handle_response(issue_info, self.serializer_class)
        except:
            return Response(
                {"error": "code is invalid"}, status=status.HTTP_400_BAD_REQUEST
            )


class MarketBondInquireDailyItemChartPriceViewSet(MarketBondBaseViewSet):
    queryset = MarketBondInquireDailyItemChartPrice.objects.all()
    serializer_class = MarketBondInquireDailyItemChartPriceSerializer

    @action(detail=False, methods=["GET"])
    def market_bond_issue_info(self, request, *args, **kwargs):
        code = request.query_params.get("code")
        bond_code, error_response = self.get_bond_code(code)
        if error_response:
            return error_response
        try:
            issue_info = self.collect_and_get_multiple_info(
                code,
                bond_code,
                MarketBondInquireDailyItemChartPrice,
                "store_market_bond_inquire_daily_itemchartprice",
            )
            serialized_data = serialize("json", issue_info)
            return Response(json.loads(serialized_data))
        except:
            return Response(
                {"error": "code is invalid"}, status=status.HTTP_400_BAD_REQUEST
            )


class MarketBondInquirePriceViewSet(MarketBondBaseViewSet):
    queryset = MarketBondInquirePrice.objects.all()
    serializer_class = MarketBondInquirePriceSerializer

    @action(detail=False, methods=["GET"])
    def market_bond_issue_info(self, request, *args, **kwargs):
        code = request.query_params.get("code")
        bond_code, error_response = self.get_bond_code(code)
        if error_response:
            return error_response
        try:
            issue_info = self.collect_and_get_info(
                code,
                bond_code,
                MarketBondInquirePrice,
                "store_market_bond_inquire_price",
            )
            return self.handle_response(issue_info, self.serializer_class)
        except:
            return Response(
                {"error": "code is invalid"}, status=status.HTTP_400_BAD_REQUEST
            )


class MarketBondInquireCCNLViewSet(MarketBondBaseViewSet):
    queryset = MarketBondInquireCCNL.objects.all()
    serializer_class = MarketBondInquireCCNLSerializer

    @action(detail=False, methods=["GET"])
    def market_bond_issue_info(self, request, *args, **kwargs):
        code = request.query_params.get("code")
        bond_code, error_response = self.get_bond_code(code)
        if error_response:
            return error_response
        try:
            issue_info = self.collect_and_get_multiple_info(
                code, bond_code, MarketBondInquireCCNL, "store_market_bond_inquire_ccnl"
            )
            # uniqueness logic needs to be added
            serialized_data = serialize("json", issue_info)

            serialized_data = serialize("json", issue_info)
            return Response(json.loads(serialized_data))

            # return Response(json.loads(serialized_data))
        except:
            return Response(
                {"error": "code is invalid"}, status=status.HTTP_400_BAD_REQUEST
            )


class MarketBondInquireDailyPriceViewSet(MarketBondBaseViewSet):
    queryset = MarketBondInquireDailyPrice.objects.all()
    serializer_class = MarketBondInquireDailyPriceSerializer

    @action(detail=False, methods=["GET"])
    def market_bond_issue_info(self, request, *args, **kwargs):
        code = request.query_params.get("code")
        bond_code, error_response = self.get_bond_code(code)
        if error_response:
            return error_response
        try:
            issue_info = self.collect_and_get_multiple_info(
                code,
                bond_code,
                MarketBondInquireDailyPrice,
                "store_market_bond_inquire_daily_price",
            )
            unique_issue_info = MarketBondInquireDailyPriceSerializer.remove_duplicates(issue_info)
            serialized_data = serialize("json", unique_issue_info)

            serialized_data = serialize("json", issue_info)
            return Response(json.loads(serialized_data))
            # return Response(json.loads(serialized_data))
        except:
            return Response(
                {"error": "code is invalid"}, status=status.HTTP_400_BAD_REQUEST
            )


class SearchKeywordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SearchKeyword.objects.all()
    serializer_class = SearchKeywordSerializer


class NaverNewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NaverNews.objects.all()
    serializer_class = NaverNewsSerializer

    @action(detail=False, methods=["GET"])
    def data(self, request, *args, **kwargs):
        query = request.query_params.get("query")
        if not query:
            return Response(
                {"error": "query is missing"}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            kw = SearchKeyword.objects.filter(search_keyword=query).first()
            if not kw:
                serializer = SearchKeywordSerializer(data={"search_keyword": query})
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(
                        {"error": "Failed to retrieve or create search_keyword"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            kw = SearchKeyword.objects.filter(search_keyword=query).first()
            getter = GetNewsData(kw.search_keyword)
            res = getter.get_naver_news_data().json()
            items = res["items"]
            for item in items:
                item["search_keyword"] = kw.id
            unique_items = NaverNewsSerializer.remove_duplicates(items)
            serializer = NaverNewsSerializer(data=unique_items, many=True)
            if serializer.is_valid():
                serializer.save()
            return Response(res)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
