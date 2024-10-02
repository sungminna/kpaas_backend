import requests
import yaml


class GetNewsData:
    def __init__(self, search_keyword):
        self.config_root = ".\\koreaib\\news_api\\"
        with open(self.config_root + "naver_api.yaml", encoding="UTF-8") as f:
            self._cfg = yaml.load(f, Loader=yaml.FullLoader)
        self._base_headers = {}
        self.query = search_keyword
        self.initialize_key()

    def initialize_key(self):
        self._base_headers = {
            "X-Naver-Client-Id": self._cfg["client_id"],
            "X-Naver-Client-Secret": self._cfg["client_secret"],
        }

    def get_naver_news_data(self):
        url = "https://openapi.naver.com/v1/search/news.json"
        payload = {"query": self.query, "sort": "date", "display": "100"}
        headers = self._base_headers
        res = requests.get(url, headers=headers, params=payload)
        return res


if __name__ == "__main__":
    s = GetNewsData()
    s.get_naver_news_data()
