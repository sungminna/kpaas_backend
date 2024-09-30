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
class MarketBondIssueInfoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MarketBondIssueInfo.objects.all()
    serializer_class = MarketBondIssueInfoSerializer

    @action(detail=False, methods=['GET'])
    def market_bond_issue_info(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        if not code:
            return Response({'error': 'code is missing'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            bond_code = MarketBondCode.objects.filter(code=code).first()
            if not bond_code:
                serializer = MarketBondCodeSerializer(data={'code': code})
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            bond_code = MarketBondCode.objects.filter(code=code).first()
            issue_info = MarketBondIssueInfo.objects.filter(code=bond_code).first()
            if not issue_info:
                collector = CollectMarketBond(code, bond_code)
                collector.store_market_bond_issue_info()
            issue_info = MarketBondIssueInfo.objects.filter(code=bond_code).first()
            if issue_info:
                serializer = self.get_serializer(issue_info)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Failed to retrieve or create issue info'}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'error': 'code is invalid'}, status=status.HTTP_400_BAD_REQUEST)


class MarketBondSearchInfoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MarketBondSearchInfo.objects.all()
    serializer_class = MarketBondSearchInfoSerializer


class MarketBondInquireAskingPriceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MarketBondInquireAskingPrice.objects.all()
    serializer_class = MarketBondInquireAskingPriceSerializer


class MarketBondAvgUnitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MarketBondAvgUnit.objects.all()
    serializer_class = MarketBondAvgUnitSerializer


class MarketBondInquireDailyItemChartPriceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MarketBondInquireDailyItemChartPrice.objects.all()
    serializer_class = MarketBondInquireDailyItemChartPriceSerializer


class MarketBondInquirePriceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MarketBondInquirePrice.objects.all()
    serializer_class = MarketBondInquirePriceSerializer


class MarketBondInquireCCNLViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MarketBondInquireCCNL.objects.all()
    serializer_class = MarketBondInquireCCNLSerializer


class MarketBondInquireDailyPriceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MarketBondInquireDailyPrice.objects.all()
    serializer_class = MarketBondInquireDailyPriceSerializer


class SearchKeywordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SearchKeyword.objects.all()
    serializer_class = SearchKeywordSerializer


class NaverNewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NaverNews.objects.all()
    serializer_class = NaverNewsSerializer
