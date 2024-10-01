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
    NaverNews
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
    NaverNewsSerializer
)

from koreaib.kib_api.collect_kis_data import CollectMarketBond

from rest_framework import viewsets, status
from rest_framework.decorators import action

class MarketBondCodeViewSet(viewsets.ModelViewSet):
    queryset = MarketBondCode.objects.all()
    serializer_class = MarketBondCodeSerializer



# Create your views here.
class MarketBondBaseViewSet(viewsets.ReadOnlyModelViewSet):
    def get_bond_code(self, code):
        if not code:
            return None, Response({'error': 'code is missing'}, status=status.HTTP_400_BAD_REQUEST)

        bond_code = MarketBondCode.objects.filter(code=code).first()
        if not bond_code:
            serializer = MarketBondCodeSerializer(data={'code': code})
            if serializer.is_valid():
                serializer.save()
            else:
                return None, Response({'error': 'Failed to retrieve or create market bond code'},
                                      status=status.HTTP_400_BAD_REQUEST)

        bond_code = MarketBondCode.objects.filter(code=code).first()
        return bond_code, None

    def collect_and_get_info(self, code, bond_code, model, collect_method):
        info = model.objects.filter(code=bond_code).first()
        if not info:
            collector = CollectMarketBond(code, bond_code)
            getattr(collector, collect_method)()
            info = model.objects.filter(code=bond_code).first()
        return info

    def handle_response(self, instance, serializer_class):
        if instance:
            serializer = serializer_class(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Failed to retrieve or create info'}, status=status.HTTP_404_NOT_FOUND)


class MarketBondIssueInfoViewSet(MarketBondBaseViewSet):
    queryset = MarketBondIssueInfo.objects.all()
    serializer_class = MarketBondIssueInfoSerializer

    @action(detail=False, methods=['GET'])
    def market_bond_issue_info(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        bond_code, error_response = self.get_bond_code(code)
        if error_response:
            return error_response
        try:
            issue_info = self.collect_and_get_info(code, bond_code, MarketBondIssueInfo, 'store_market_bond_issue_info')
            return self.handle_response(issue_info, self.serializer_class)
        except:
            return Response({'error': 'code is invalid'}, status=status.HTTP_400_BAD_REQUEST)


class MarketBondSearchInfoViewSet(MarketBondBaseViewSet):
    queryset = MarketBondSearchInfo.objects.all()
    serializer_class = MarketBondSearchInfoSerializer

    @action(detail=False, methods=['GET'])
    def market_bond_issue_info(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        bond_code, error_response = self.get_bond_code(code)
        if error_response:
            return error_response
        try:
            issue_info = self.collect_and_get_info(code, bond_code, MarketBondSearchInfo, 'store_market_bond_search_info')
            return self.handle_response(issue_info, self.serializer_class)
        except:
            return Response({'error': 'code is invalid'}, status=status.HTTP_400_BAD_REQUEST)


class MarketBondInquireAskingPriceViewSet(MarketBondBaseViewSet):
    queryset = MarketBondInquireAskingPrice.objects.all()
    serializer_class = MarketBondInquireAskingPriceSerializer

    @action(detail=False, methods=['GET'])
    def market_bond_issue_info(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        bond_code, error_response = self.get_bond_code(code)
        if error_response:
            return error_response
        try:
            issue_info = self.collect_and_get_info(code, bond_code, MarketBondInquireAskingPrice, 'store_market_bond_inquire_asking_price')
            return self.handle_response(issue_info, self.serializer_class)
        except:
            return Response({'error': 'code is invalid'}, status=status.HTTP_400_BAD_REQUEST)


class MarketBondAvgUnitViewSet(MarketBondBaseViewSet):
    queryset = MarketBondAvgUnit.objects.all()
    serializer_class = MarketBondAvgUnitSerializer

    @action(detail=False, methods=['GET'])
    def market_bond_issue_info(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        bond_code, error_response = self.get_bond_code(code)
        if error_response:
            return error_response
        try:
            issue_info = self.collect_and_get_info(code, bond_code, MarketBondAvgUnit, 'store_market_bond_avg_unit')
            return self.handle_response(issue_info, self.serializer_class)
        except:
            return Response({'error': 'code is invalid'}, status=status.HTTP_400_BAD_REQUEST)


class MarketBondInquireDailyItemChartPriceViewSet(MarketBondBaseViewSet):
    queryset = MarketBondInquireDailyItemChartPrice.objects.all()
    serializer_class = MarketBondInquireDailyItemChartPriceSerializer

    @action(detail=False, methods=['GET'])
    def market_bond_issue_info(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        bond_code, error_response = self.get_bond_code(code)
        if error_response:
            return error_response
        try:
            issue_info = self.collect_and_get_info(code, bond_code, MarketBondInquireDailyItemChartPrice, 'store_market_bond_inquire_daily_itemchartprice')
            return self.handle_response(issue_info, self.serializer_class)
        except:
            return Response({'error': 'code is invalid'}, status=status.HTTP_400_BAD_REQUEST)


class MarketBondInquirePriceViewSet(MarketBondBaseViewSet):
    queryset = MarketBondInquirePrice.objects.all()
    serializer_class = MarketBondInquirePriceSerializer

    @action(detail=False, methods=['GET'])
    def market_bond_issue_info(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        bond_code, error_response = self.get_bond_code(code)
        if error_response:
            return error_response
        try:
            issue_info = self.collect_and_get_info(code, bond_code, MarketBondInquirePrice, 'store_market_bond_inquire_price')
            return self.handle_response(issue_info, self.serializer_class)
        except:
            return Response({'error': 'code is invalid'}, status=status.HTTP_400_BAD_REQUEST)


class MarketBondInquireCCNLViewSet(MarketBondBaseViewSet):
    queryset = MarketBondInquireCCNL.objects.all()
    serializer_class = MarketBondInquireCCNLSerializer

    @action(detail=False, methods=['GET'])
    def market_bond_issue_info(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        bond_code, error_response = self.get_bond_code(code)
        if error_response:
            return error_response
        try:
            issue_info = self.collect_and_get_info(code, bond_code, MarketBondInquireCCNL, 'store_market_bond_inquire_ccnl')
            return self.handle_response(issue_info, self.serializer_class)
        except:
            return Response({'error': 'code is invalid'}, status=status.HTTP_400_BAD_REQUEST)


class MarketBondInquireDailyPriceViewSet(MarketBondBaseViewSet):
    queryset = MarketBondInquireDailyPrice.objects.all()
    serializer_class = MarketBondInquireDailyPriceSerializer

    @action(detail=False, methods=['GET'])
    def market_bond_issue_info(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        bond_code, error_response = self.get_bond_code(code)
        if error_response:
            return error_response
        try:
            issue_info = self.collect_and_get_info(code, bond_code, MarketBondInquireDailyPrice, 'store_market_bond_inquire_daily_price')
            return self.handle_response(issue_info, self.serializer_class)
        except:
            return Response({'error': 'code is invalid'}, status=status.HTTP_400_BAD_REQUEST)


class SearchKeywordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SearchKeyword.objects.all()
    serializer_class = SearchKeywordSerializer


class NaverNewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NaverNews.objects.all()
    serializer_class = NaverNewsSerializer
