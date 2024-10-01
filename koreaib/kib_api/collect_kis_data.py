from koreaib.models import (
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

from koreaib.serializer import (
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


from koreaib.kib_api.get_rest_data import GetRestData


class CollectMarketBond:
    def __init__(self, pdno="KR6150351E98", bond_code=""):
        self.pdno = pdno
        self.bond_code = bond_code
        self.data_getter = GetRestData(pdno=self.pdno, bond_code=self.bond_code)

    def store_market_bond_issue_info(self):
        data = self.data_getter.get_issue_info()
        serializer = MarketBondIssueInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

    def store_market_bond_search_info(self):
        data = self.data_getter.get_search_bond_info()
        serializer = MarketBondSearchInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

    def store_market_bond_inquire_asking_price(self):
        data = self.data_getter.get_inquire_asking_price()
        serializer = MarketBondInquireAskingPriceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data

    def store_market_bond_avg_unit(self):
        data = self.data_getter.get_avg_unit()
        serializer = MarketBondAvgUnitSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data

    def store_market_bond_inquire_daily_itemchartprice(self):
        data = self.data_getter.get_inquire_daily_itemchartprice()
        serializer = MarketBondInquireDailyItemChartPriceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

    def store_market_bond_inquire_price(self):
        data = self.data_getter.get_inquire_price()
        serializer = MarketBondInquirePriceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

    def store_market_bond_inquire_ccnl(self):
        data = self.data_getter.get_inquire_ccnl()
        serializer = MarketBondInquireCCNLSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

    def store_market_bond_inquire_daily_price(self):
        data = self.data_getter.get_inquire_daily_price()
        serializer = MarketBondInquireDailyPriceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

    def store_market_search_bond_info(self):
        data = self.data_getter.get_search_bond_info()
        serializer = MarketBondSearchInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
