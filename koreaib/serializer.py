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
        fields = "__all__"


class MarketBondIssueInfoSerializer(serializers.ModelSerializer):
    code = serializers.PrimaryKeyRelatedField(queryset=MarketBondCode.objects.all())

    class Meta:
        model = MarketBondIssueInfo
        fields = "__all__"
        extra_kwargs = {
            "pdno": {"allow_blank": True},
            "prdt_type_cd": {"allow_blank": True},
            "prdt_name": {"allow_blank": True},
            "prdt_eng_name": {"allow_blank": True},
            "ivst_heed_prdt_yn": {"allow_blank": True},
            "exts_yn": {"allow_blank": True},
            "bond_clsf_cd": {"allow_blank": True},
            "bond_clsf_kor_name": {"allow_blank": True},
            "papr": {"allow_blank": True},
            "int_mned_dvsn_cd": {"allow_blank": True},
            "rvnu_shap_cd": {"allow_blank": True},
            "issu_amt": {"allow_blank": True},
            "lstg_rmnd": {"allow_blank": True},
            "int_dfrm_mcnt": {"allow_blank": True},
            "bond_int_dfrm_mthd_cd": {"allow_blank": True},
            "splt_rdpt_rcnt": {"allow_blank": True},
            "prca_dfmt_term_mcnt": {"allow_blank": True},
            "int_anap_dvsn_cd": {"allow_blank": True},
            "bond_rght_dvsn_cd": {"allow_blank": True},
            "prdt_pclc_text": {"allow_blank": True},
            "prdt_abrv_name": {"allow_blank": True},
            "prdt_eng_abrv_name": {"allow_blank": True},
            "sprx_psbl_yn": {"allow_blank": True},
            "pbff_pplc_ofrg_mthd_cd": {"allow_blank": True},
            "cmco_cd": {"allow_blank": True},
            "issu_istt_cd": {"allow_blank": True},
            "issu_istt_name": {"allow_blank": True},
            "pnia_dfrm_agcy_istt_cd": {"allow_blank": True},
            "dsct_ec_rt": {"allow_blank": True},
            "srfc_inrt": {"allow_blank": True},
            "expd_rdpt_rt": {"allow_blank": True},
            "expd_asrc_erng_rt": {"allow_blank": True},
            "bond_grte_istt_name": {"allow_blank": True},
            "int_dfrm_day_type_cd": {"allow_blank": True},
            "ksd_int_calc_unit_cd": {"allow_blank": True},
            "int_wunt_uder_prcs_dvsn_cd": {"allow_blank": True},
            "rvnu_dt": {"allow_blank": True},
            "issu_dt": {"allow_blank": True},
            "lstg_dt": {"allow_blank": True},
            "expd_dt": {"allow_blank": True},
            "rdpt_dt": {"allow_blank": True},
            "sbst_pric": {"allow_blank": True},
            "rgbf_int_dfrm_dt": {"allow_blank": True},
            "nxtm_int_dfrm_dt": {"allow_blank": True},
            "frst_int_dfrm_dt": {"allow_blank": True},
            "ecis_pric": {"allow_blank": True},
            "rght_stck_std_pdno": {"allow_blank": True},
            "ecis_opng_dt": {"allow_blank": True},
            "ecis_end_dt": {"allow_blank": True},
            "bond_rvnu_mthd_cd": {"allow_blank": True},
            "oprt_stfno": {"allow_blank": True},
            "oprt_stff_name": {"allow_blank": True},
            "rgbf_int_dfrm_wday": {"allow_blank": True},
            "nxtm_int_dfrm_wday": {"allow_blank": True},
            "kis_crdt_grad_text": {"allow_blank": True},
            "kbp_crdt_grad_text": {"allow_blank": True},
            "nice_crdt_grad_text": {"allow_blank": True},
            "fnp_crdt_grad_text": {"allow_blank": True},
            "dpsi_psbl_yn": {"allow_blank": True},
            "pnia_int_calc_unpr": {"allow_blank": True},
            "prcm_idx_bond_yn": {"allow_blank": True},
            "expd_exts_srdp_rcnt": {"allow_blank": True},
            "expd_exts_srdp_rt": {"allow_blank": True},
            "loan_psbl_yn": {"allow_blank": True},
            "grte_dvsn_cd": {"allow_blank": True},
            "fnrr_rank_dvsn_cd": {"allow_blank": True},
            "krx_lstg_abol_dvsn_cd": {"allow_blank": True},
            "asst_rqdi_dvsn_cd": {"allow_blank": True},
            "opcb_dvsn_cd": {"allow_blank": True},
            "crfd_item_yn": {"allow_blank": True},
            "crfd_item_rstc_cclc_dt": {"allow_blank": True},
            "bond_nmpr_unit_pric": {"allow_blank": True},
            "ivst_heed_bond_dvsn_name": {"allow_blank": True},
            "add_erng_rt": {"allow_blank": True},
            "add_erng_rt_aply_dt": {"allow_blank": True},
            "bond_tr_stop_dvsn_cd": {"allow_blank": True},
            "ivst_heed_bond_dvsn_cd": {"allow_blank": True},
            "pclr_cndt_text": {"allow_blank": True},
            "hbbd_yn": {"allow_blank": True},
            "cdtl_cptl_scty_type_cd": {"allow_blank": True},
            "elec_scty_yn": {"allow_blank": True},
            "sq1_clop_ecis_opng_dt": {"allow_blank": True},
            "frst_erlm_stfno": {"allow_blank": True},
            "frst_erlm_dt": {"allow_blank": True},
            "frst_erlm_tmd": {"allow_blank": True},
        }


class MarketBondSearchInfoSerializer(serializers.ModelSerializer):
    code = serializers.PrimaryKeyRelatedField(queryset=MarketBondCode.objects.all())

    class Meta:
        model = MarketBondSearchInfo
        fields = "__all__"
        extra_kwargs = {
            "pdno": {"allow_blank": True},
            "prdt_type_cd": {"allow_blank": True},
            "ksd_bond_item_name": {"allow_blank": True},
            "ksd_bond_item_eng_name": {"allow_blank": True},
            "ksd_bond_lstg_type_cd": {"allow_blank": True},
            "ksd_ofrg_dvsn_cd": {"allow_blank": True},
            "ksd_bond_int_dfrm_dvsn_cd": {"allow_blank": True},
            "issu_dt": {"allow_blank": True},
            "rdpt_dt": {"allow_blank": True},
            "rvnu_dt": {"allow_blank": True},
            "iso_crcy_cd": {"allow_blank": True},
            "mdwy_rdpt_dt": {"allow_blank": True},
            "ksd_rcvg_bond_dsct_rt": {"allow_blank": True},
            "ksd_rcvg_bond_srfc_inrt": {"allow_blank": True},
            "bond_expd_rdpt_rt": {"allow_blank": True},
            "ksd_prca_rdpt_mthd_cd": {"allow_blank": True},
            "int_caltm_mcnt": {"allow_blank": True},
            "ksd_int_calc_unit_cd": {"allow_blank": True},
            "uval_cut_dvsn_cd": {"allow_blank": True},
            "uval_cut_dcpt_dgit": {"allow_blank": True},
            "ksd_dydv_caltm_aply_dvsn_cd": {"allow_blank": True},
            "dydv_calc_dcnt": {"allow_blank": True},
            "bond_expd_asrc_erng_rt": {"allow_blank": True},
            "padf_plac_hdof_name": {"allow_blank": True},
            "lstg_dt": {"allow_blank": True},
            "lstg_abol_dt": {"allow_blank": True},
            "ksd_bond_issu_mthd_cd": {"allow_blank": True},
            "laps_indf_yn": {"allow_blank": True},
            "ksd_lhdy_pnia_dfrm_mthd_cd": {"allow_blank": True},
            "frst_int_dfrm_dt": {"allow_blank": True},
            "ksd_prcm_lnkg_gvbd_yn": {"allow_blank": True},
            "dpsi_end_dt": {"allow_blank": True},
            "dpsi_strt_dt": {"allow_blank": True},
            "dpsi_psbl_yn": {"allow_blank": True},
            "atyp_rdpt_bond_erlm_yn": {"allow_blank": True},
            "dshn_occr_yn": {"allow_blank": True},
            "expd_exts_yn": {"allow_blank": True},
            "pclr_ptcr_text": {"allow_blank": True},
            "dpsi_psbl_excp_stat_cd": {"allow_blank": True},
            "expd_exts_srdp_rcnt": {"allow_blank": True},
            "expd_exts_srdp_rt": {"allow_blank": True},
            "expd_rdpt_rt": {"allow_blank": True},
            "expd_asrc_erng_rt": {"allow_blank": True},
            "bond_int_dfrm_mthd_cd": {"allow_blank": True},
            "int_dfrm_day_type_cd": {"allow_blank": True},
            "prca_dfmt_term_mcnt": {"allow_blank": True},
            "splt_rdpt_rcnt": {"allow_blank": True},
            "rgbf_int_dfrm_dt": {"allow_blank": True},
            "nxtm_int_dfrm_dt": {"allow_blank": True},
            "sprx_psbl_yn": {"allow_blank": True},
            "ictx_rt_dvsn_cd": {"allow_blank": True},
            "bond_clsf_cd": {"allow_blank": True},
            "bond_clsf_kor_name": {"allow_blank": True},
            "int_mned_dvsn_cd": {"allow_blank": True},
            "pnia_int_calc_unpr": {"allow_blank": True},
            "frn_intr": {"allow_blank": True},
            "aply_day_prcm_idx_lnkg_cefc": {"allow_blank": True},
            "ksd_expd_dydv_calc_bass_cd": {"allow_blank": True},
            "expd_dydv_calc_dcnt": {"allow_blank": True},
            "ksd_cbbw_dvsn_cd": {"allow_blank": True},
            "crfd_item_yn": {"allow_blank": True},
            "pnia_bank_ofdy_dfrm_mthd_cd": {"allow_blank": True},
            "qib_yn": {"allow_blank": True},
            "qib_cclc_dt": {"allow_blank": True},
            "csbd_yn": {"allow_blank": True},
            "csbd_cclc_dt": {"allow_blank": True},
            "ksd_opcb_yn": {"allow_blank": True},
            "ksd_sodn_yn": {"allow_blank": True},
            "ksd_rqdi_scty_yn": {"allow_blank": True},
            "elec_scty_yn": {"allow_blank": True},
            "rght_ecis_mbdy_dvsn_cd": {"allow_blank": True},
            "int_rkng_mthd_dvsn_cd": {"allow_blank": True},
            "ofrg_dvsn_cd": {"allow_blank": True},
            "ksd_tot_issu_amt": {"allow_blank": True},
            "next_indf_chk_ecls_yn": {"allow_blank": True},
            "ksd_bond_intr_dvsn_cd": {"allow_blank": True},
            "ksd_inrt_aply_dvsn_cd": {"allow_blank": True},
            "krx_issu_istt_cd": {"allow_blank": True},
            "ksd_indf_frqc_uder_calc_cd": {"allow_blank": True},
            "ksd_indf_frqc_uder_calc_dcnt": {"allow_blank": True},
            "tlg_rcvg_dtl_dtime": {"allow_blank": True},
        }


class MarketBondInquireAskingPriceSerializer(serializers.ModelSerializer):
    code = serializers.PrimaryKeyRelatedField(queryset=MarketBondCode.objects.all())

    class Meta:
        model = MarketBondInquireAskingPrice
        fields = "__all__"
        extra_kwargs = {
            "aspr_acpt_hour": {"allow_blank": True},
            "bond_askp1": {"allow_blank": True},
            "bond_askp2": {"allow_blank": True},
            "bond_askp3": {"allow_blank": True},
            "bond_askp4": {"allow_blank": True},
            "bond_askp5": {"allow_blank": True},
            "bond_bidp1": {"allow_blank": True},
            "bond_bidp2": {"allow_blank": True},
            "bond_bidp3": {"allow_blank": True},
            "bond_bidp4": {"allow_blank": True},
            "bond_bidp5": {"allow_blank": True},
            "askp_rsqn1": {"allow_blank": True},
            "askp_rsqn2": {"allow_blank": True},
            "askp_rsqn3": {"allow_blank": True},
            "askp_rsqn4": {"allow_blank": True},
            "askp_rsqn5": {"allow_blank": True},
            "bidp_rsqn1": {"allow_blank": True},
            "bidp_rsqn2": {"allow_blank": True},
            "bidp_rsqn3": {"allow_blank": True},
            "bidp_rsqn4": {"allow_blank": True},
            "bidp_rsqn5": {"allow_blank": True},
            "total_askp_rsqn": {"allow_blank": True},
            "total_bidp_rsqn": {"allow_blank": True},
            "ntby_aspr_rsqn": {"allow_blank": True},
            "seln_ernn_rate1": {"allow_blank": True},
            "seln_ernn_rate2": {"allow_blank": True},
            "seln_ernn_rate3": {"allow_blank": True},
            "seln_ernn_rate4": {"allow_blank": True},
            "seln_ernn_rate5": {"allow_blank": True},
            "shnu_ernn_rate1": {"allow_blank": True},
            "shnu_ernn_rate2": {"allow_blank": True},
            "shnu_ernn_rate3": {"allow_blank": True},
            "shnu_ernn_rate4": {"allow_blank": True},
            "shnu_ernn_rate5": {"allow_blank": True},
        }


class MarketBondAvgUnitSerializer(serializers.ModelSerializer):
    code = serializers.PrimaryKeyRelatedField(queryset=MarketBondCode.objects.all())

    class Meta:
        model = MarketBondAvgUnit
        fields = "__all__"


class MarketBondInquireDailyItemChartPriceSerializer(serializers.ModelSerializer):
    code = serializers.PrimaryKeyRelatedField(queryset=MarketBondCode.objects.all())

    class Meta:
        model = MarketBondInquireDailyItemChartPrice
        fields = "__all__"
        extra_kwargs = {
            "stck_bsop_date": {"allow_blank": True},
            "bond_oprc": {"allow_blank": True},
            "bond_hgpr": {"allow_blank": True},
            "bond_lwpr": {"allow_blank": True},
            "bond_prpr": {"allow_blank": True},
            "acml_vol": {"allow_blank": True},
        }


class MarketBondInquirePriceSerializer(serializers.ModelSerializer):
    code = serializers.PrimaryKeyRelatedField(queryset=MarketBondCode.objects.all())

    class Meta:
        model = MarketBondInquirePrice
        fields = "__all__"
        extra_kwargs = {
            "stnd_iscd": {"allow_blank": True},
            "hts_kor_isnm": {"allow_blank": True},
            "bond_prpr": {"allow_blank": True},
            "prdy_vrss_sign": {"allow_blank": True},
            "bond_prdy_vrss": {"allow_blank": True},
            "prdy_ctrt": {"allow_blank": True},
            "acml_vol": {"allow_blank": True},
            "bond_prdy_clpr": {"allow_blank": True},
            "bond_oprc": {"allow_blank": True},
            "bond_hgpr": {"allow_blank": True},
            "bond_lwpr": {"allow_blank": True},
            "ernn_rate": {"allow_blank": True},
            "oprc_ert": {"allow_blank": True},
            "hgpr_ert": {"allow_blank": True},
            "lwpr_ert": {"allow_blank": True},
            "bond_mxpr": {"allow_blank": True},
            "bond_llam": {"allow_blank": True},
        }


class MarketBondInquireCCNLSerializer(serializers.ModelSerializer):
    code = serializers.PrimaryKeyRelatedField(queryset=MarketBondCode.objects.all())

    class Meta:
        model = MarketBondInquireCCNL
        fields = "__all__"
        extra_kwargs = {
            "stck_cntg_hour": {"allow_blank": True},
            "bond_prpr": {"allow_blank": True},
            "bond_prdy_vrss": {"allow_blank": True},
            "prdy_vrss_sign": {"allow_blank": True},
            "prdy_ctrt": {"allow_blank": True},
            "cntg_vol": {"allow_blank": True},
            "acml_vol": {"allow_blank": True},
        }


class MarketBondInquireDailyPriceSerializer(serializers.ModelSerializer):
    code = serializers.PrimaryKeyRelatedField(queryset=MarketBondCode.objects.all())

    class Meta:
        model = MarketBondInquireDailyPrice
        fields = "__all__"
        extra_kwargs = {
            "stck_bsop_date": {"allow_blank": True},
            "bond_prpr": {"allow_blank": True},
            "bond_prdy_vrss": {"allow_blank": True},
            "prdy_vrss_sign": {"allow_blank": True},
            "prdy_ctrt": {"allow_blank": True},
            "acml_vol": {"allow_blank": True},
            "bond_oprc": {"allow_blank": True},
            "bond_hgpr": {"allow_blank": True},
            "bond_lwpr": {"allow_blank": True},
        }


class SearchKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchKeyword
        fields = "__all__"


class NaverNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = NaverNews
        fields = "__all__"
