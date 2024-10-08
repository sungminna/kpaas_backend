from rest_framework.routers import DefaultRouter

from .views import (
    MarketBondCodeViewSet,
    MarketBondIssueInfoViewSet,
    MarketBondSearchInfoViewSet,
    MarketBondInquireAskingPriceViewSet,
    MarketBondAvgUnitViewSet,
    MarketBondInquireDailyItemChartPriceViewSet,
    MarketBondInquirePriceViewSet,
    MarketBondInquireCCNLViewSet,
    MarketBondInquireDailyPriceViewSet,
    NaverNewsViewSet,
)

router = DefaultRouter()
router.register("market-bond-code", MarketBondCodeViewSet)
router.register("market-bond-issue-info", MarketBondIssueInfoViewSet)
router.register("market-bond-search-info", MarketBondSearchInfoViewSet)
router.register("market-bond-inquire-asking-price", MarketBondInquireAskingPriceViewSet)
router.register("market-bond-avg-unit", MarketBondAvgUnitViewSet)
router.register(
    "market-bond-inquire-daily-item-chart-price",
    MarketBondInquireDailyItemChartPriceViewSet,
)
router.register("market-bond-inquire-price", MarketBondInquirePriceViewSet)
router.register("market-bond-inquire-ccnl", MarketBondInquireCCNLViewSet)
router.register("market-bond-inquire-daily-price", MarketBondInquireDailyPriceViewSet)
router.register("news", NaverNewsViewSet)


urlpatterns = router.urls
