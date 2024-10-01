from koreaib.kib_api.kis_auth import KisAuth
import json


class GetRestData:
    def __init__(self, pdno="KR6150351E98", bond_code=""):
        self.kis = KisAuth()
        self.kis.auth()
        self.pdno = pdno  # KR6150351E98
        self.bond_code = bond_code

    # 장내채권 발행정보
    def get_issue_info(self):
        url = "/uapi/domestic-bond/v1/quotations/issue-info"
        ptr_id = "CTPF1101R"
        tr_cont = ""

        params = {
            "PDNO": self.pdno,  # 시장 분류 코드
            "PRDT_TYPE_CD": "302",  # 화면 분류 코드
        }
        res = self.kis._url_fetch(
            url,
            ptr_id,
            tr_cont,
            params,
        )
        dic = res.getBody().output
        dic["code"] = self.bond_code.id
        # data = json.dumps(dic)
        return dic

    # 장내채권현재가(호가)
    def get_inquire_asking_price(self):
        url = "/uapi/domestic-bond/v1/quotations/inquire-asking-price"
        ptr_id = "FHKBJ773401C0"
        tr_cont = ""

        params = {
            "FID_COND_MRKT_DIV_CODE": "B",  # 시장 분류 코드
            "FID_INPUT_ISCD": self.pdno,  # 채권종목코드
        }

        res = self.kis._url_fetch(
            url,
            ptr_id,
            tr_cont,
            params,
        )
        dic = res.getBody().output
        dic["code"] = self.bond_code.id
        return dic

    # 장내채권 평균단가조회
    def get_avg_unit(self):
        url = "/uapi/domestic-bond/v1/quotations/avg-unit"
        ptr_id = "CTPF2005R"
        tr_cont = ""

        params = {
            "INQR_STRT_DT": "20240101",  # 조회 시작 일자
            "INQR_END_DT": "20240425",  # 조회 종료 일자
            "PDNO": self.pdno,  # 종목 코드
            "PRDT_TYPE_CD": "302",  # 상품유형코드
            "VRFC_KIND_CD": "00",  # 검증종류코드
            "CTX_AREA_NK30": "",  # 연속조회키30
            "CTX_AREA_FK100": "",  # 연속조회검색조건100
        }

        res = self.kis._url_fetch(
            url,
            ptr_id,
            tr_cont,
            params,
        )
        dic = res.getBody().output
        dic["code"] = self.bond_code.id
        return dic

    # 장내채권 기간별시세(일)
    def get_inquire_daily_itemchartprice(self):
        url = "/uapi/domestic-bond/v1/quotations/inquire-daily-itemchartprice"
        ptr_id = "FHKBJ773701C0"
        tr_cont = ""

        params = {
            "FID_COND_MRKT_DIV_CODE": "B",  # 시장 구분 코드
            "FID_INPUT_ISCD": self.pdno,  # 채권종목코드
        }

        res = self.kis._url_fetch(
            url,
            ptr_id,
            tr_cont,
            params,
        )
        dic = res.getBody().output
        for item in dic:
            item["code"] = self.bond_code.id
        return dic

    # 장내채권현재가(시세)
    def get_inquire_price(self):
        url = "/uapi/domestic-bond/v1/quotations/inquire-price"
        ptr_id = "FHKBJ773400C0"
        tr_cont = ""

        params = {
            "FID_COND_MRKT_DIV_CODE": "B",  # 시장 구분 코드
            "FID_INPUT_ISCD": self.pdno,  # 채권종목코드
        }

        res = self.kis._url_fetch(
            url,
            ptr_id,
            tr_cont,
            params,
        )
        dic = res.getBody().output
        dic["code"] = self.bond_code.id
        return dic

    # 장내채권현재가(체결)
    def get_inquire_ccnl(self):
        url = "/uapi/domestic-bond/v1/quotations/inquire-ccnl"
        ptr_id = "FHKBJ773403C0"
        tr_cont = ""

        params = {
            "FID_COND_MRKT_DIV_CODE": "B",  # 시장 구분 코드
            "FID_INPUT_ISCD": self.pdno,  # 채권종목코드
        }

        res = self.kis._url_fetch(
            url,
            ptr_id,
            tr_cont,
            params,
        )
        dic = res.getBody().output
        dic["code"] = self.bond_code.id
        return dic

    # 장내채권현재가(일별)
    def get_inquire_daily_price(self):
        url = "/uapi/domestic-bond/v1/quotations/inquire-daily-price"
        ptr_id = "FHKBJ773404C0"
        tr_cont = ""

        params = {
            "FID_COND_MRKT_DIV_CODE": "B",  # 시장 구분 코드
            "FID_INPUT_ISCD": self.pdno,  # 채권종목코드
        }

        res = self.kis._url_fetch(
            url,
            ptr_id,
            tr_cont,
            params,
        )
        dic = res.getBody().output
        for item in dic:
            item["code"] = self.bond_code.id
        return dic

    # 장내채권 기본조회
    def get_search_bond_info(self):
        url = "/uapi/domestic-bond/v1/quotations/search-bond-info"
        ptr_id = "CTPF1114R"
        tr_cont = ""

        params = {
            "PDNO": self.pdno,  # 채권종목코드
            "PRDT_TYPE_CD": "302",  # 상품유형코드
        }
        res = self.kis._url_fetch(
            url,
            ptr_id,
            tr_cont,
            params,
        )
        dic = res.getBody().output
        dic["code"] = self.bond_code.id
        return dic


if __name__ == "__main__":
    re = GetRestData()
    re.get_issue_info()
