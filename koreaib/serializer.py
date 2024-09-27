from rest_framework import serializers
from .models import MarketBondIssueInfo, MarketBondSearchInfo, MarketBondInquireAskingPrice, MarketBondAvgUnit, \
                    MarketBondInquireDailyItemChartPrice, MarketBondInquirePrice, MarketBondInquireCCNL, \
                    MarketBondInquireDailyPrice


class MarketBondIssueInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketBondIssueInfo
        fields = '__all__'


class MarketBondSearchInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketBondSearchInfo
        fields = '__all__'


class MarketBondInquireAskingPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketBondInquireAskingPrice
        fields = '__all__'


class MarketBondAvgUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketBondAvgUnit
        fields = '__all__'


class MarketBondInquireDailyItemChartPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketBondInquireDailyItemChartPrice
        fields = '__all__'


class MarketBondInquirePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketBondInquirePrice
        fields = '__all__'


class MarketBondInquireCCNLSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketBondInquireCCNL
        fields = '__all__'


class MarketBondInquireDailyPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketBondInquireDailyPrice
        fields = '__all__'
