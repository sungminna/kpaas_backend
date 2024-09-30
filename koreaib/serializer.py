from rest_framework import serializers
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


class MarketBondCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketBondCode
        fields = '__all__'


class MarketBondIssueInfoSerializer(serializers.ModelSerializer):
    code = serializers.PrimaryKeyRelatedField(queryset=MarketBondCode.objects.all())
    class Meta:
        model = MarketBondIssueInfo
        fields = "__all__"


class MarketBondSearchInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketBondSearchInfo
        fields = "__all__"


class MarketBondInquireAskingPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketBondInquireAskingPrice
        fields = "__all__"


class MarketBondAvgUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketBondAvgUnit
        fields = "__all__"


class MarketBondInquireDailyItemChartPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketBondInquireDailyItemChartPrice
        fields = "__all__"


class MarketBondInquirePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketBondInquirePrice
        fields = "__all__"


class MarketBondInquireCCNLSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketBondInquireCCNL
        fields = "__all__"


class MarketBondInquireDailyPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketBondInquireDailyPrice
        fields = "__all__"


class SearchKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchKeyword
        fields = "__all__"


class NaverNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = NaverNews
        fields = "__all__"
