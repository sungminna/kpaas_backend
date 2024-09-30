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
        extra_kwargs = {
            'pdno': {'allow_blank': True},
            'prdt_type_cd': {'allow_blank': True},
            'prdt_name': {'allow_blank': True},
            'prdt_eng_name': {'allow_blank': True},
            'ivst_heed_prdt_yn': {'allow_blank': True},
            'exts_yn': {'allow_blank': True},
            'bond_clsf_cd': {'allow_blank': True},
            'bond_clsf_kor_name': {'allow_blank': True},
            'papr': {'allow_blank': True},
            'int_mned_dvsn_cd': {'allow_blank': True},
            'rvnu_shap_cd': {'allow_blank': True},
            'issu_amt': {'allow_blank': True},
            'lstg_rmnd': {'allow_blank': True},
            'int_dfrm_mcnt': {'allow_blank': True},
            'bond_int_dfrm_mthd_cd': {'allow_blank': True},
            'splt_rdpt_rcnt': {'allow_blank': True},
            'prca_dfmt_term_mcnt': {'allow_blank': True},
            'int_anap_dvsn_cd': {'allow_blank': True},
            'bond_rght_dvsn_cd': {'allow_blank': True},
            'prdt_pclc_text': {'allow_blank': True},
            'prdt_abrv_name': {'allow_blank': True},
            'prdt_eng_abrv_name': {'allow_blank': True},
            'sprx_psbl_yn': {'allow_blank': True},
            'pbff_pplc_ofrg_mthd_cd': {'allow_blank': True},
            'cmco_cd': {'allow_blank': True},
            'issu_istt_cd': {'allow_blank': True},
            'issu_istt_name': {'allow_blank': True},
            'pnia_dfrm_agcy_istt_cd': {'allow_blank': True},
            'dsct_ec_rt': {'allow_blank': True},
            'srfc_inrt': {'allow_blank': True},
            'expd_rdpt_rt': {'allow_blank': True},
            'expd_asrc_erng_rt': {'allow_blank': True},
            'bond_grte_istt_name': {'allow_blank': True},
            'int_dfrm_day_type_cd': {'allow_blank': True},
            'ksd_int_calc_unit_cd': {'allow_blank': True},
            'int_wunt_uder_prcs_dvsn_cd': {'allow_blank': True},
            'rvnu_dt': {'allow_blank': True},
            'issu_dt': {'allow_blank': True},
            'lstg_dt': {'allow_blank': True},
            'expd_dt': {'allow_blank': True},
            'rdpt_dt': {'allow_blank': True},
            'sbst_pric': {'allow_blank': True},
            'rgbf_int_dfrm_dt': {'allow_blank': True},
            'nxtm_int_dfrm_dt': {'allow_blank': True},
            'frst_int_dfrm_dt': {'allow_blank': True},
            'ecis_pric': {'allow_blank': True},
            'rght_stck_std_pdno': {'allow_blank': True},
            'ecis_opng_dt': {'allow_blank': True},
            'ecis_end_dt': {'allow_blank': True},
            'bond_rvnu_mthd_cd': {'allow_blank': True},
            'oprt_stfno': {'allow_blank': True},
            'oprt_stff_name': {'allow_blank': True},
            'rgbf_int_dfrm_wday': {'allow_blank': True},
            'nxtm_int_dfrm_wday': {'allow_blank': True},
            'kis_crdt_grad_text': {'allow_blank': True},
            'kbp_crdt_grad_text': {'allow_blank': True},
            'nice_crdt_grad_text': {'allow_blank': True},
            'fnp_crdt_grad_text': {'allow_blank': True},
            'dpsi_psbl_yn': {'allow_blank': True},
            'pnia_int_calc_unpr': {'allow_blank': True},
            'prcm_idx_bond_yn': {'allow_blank': True},
            'expd_exts_srdp_rcnt': {'allow_blank': True},
            'expd_exts_srdp_rt': {'allow_blank': True},
            'loan_psbl_yn': {'allow_blank': True},
            'grte_dvsn_cd': {'allow_blank': True},
            'fnrr_rank_dvsn_cd': {'allow_blank': True},
            'krx_lstg_abol_dvsn_cd': {'allow_blank': True},
            'asst_rqdi_dvsn_cd': {'allow_blank': True},
            'opcb_dvsn_cd': {'allow_blank': True},
            'crfd_item_yn': {'allow_blank': True},
            'crfd_item_rstc_cclc_dt': {'allow_blank': True},
            'bond_nmpr_unit_pric': {'allow_blank': True},
            'ivst_heed_bond_dvsn_name': {'allow_blank': True},
            'add_erng_rt': {'allow_blank': True},
            'add_erng_rt_aply_dt': {'allow_blank': True},
            'bond_tr_stop_dvsn_cd': {'allow_blank': True},
            'ivst_heed_bond_dvsn_cd': {'allow_blank': True},
            'pclr_cndt_text': {'allow_blank': True},
            'hbbd_yn': {'allow_blank': True},
            'cdtl_cptl_scty_type_cd': {'allow_blank': True},
            'elec_scty_yn': {'allow_blank': True},
            'sq1_clop_ecis_opng_dt': {'allow_blank': True},
            'frst_erlm_stfno': {'allow_blank': True},
            'frst_erlm_dt': {'allow_blank': True},
            'frst_erlm_tmd': {'allow_blank': True},
        }


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
