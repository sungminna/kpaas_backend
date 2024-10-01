import requests
import yaml


class GetNewsData:
    def __init__(self):
        config_root = ".\\"
        with open(config_root + "naver_api.yaml", encoding="UTF-8") as f:
            self._cfg = yaml.load(f, Loader=yaml.FullLoader)
        self._base_headers = {}
        self.query = "삼성"
        self.initialize_key()

    def initialize_key(self):
        config_root = ".\\"
        self._base_headers = {
            "X-Naver-Client-Id": self._cfg["client_id"],
            "X-Naver-Client-Secret": self._cfg["client_secret"],
        }

    def get_naver_news_data(self):
        url = "https://openapi.naver.com/v1/search/news.json"
        payload = {"query": self.query}
        headers = self._base_headers
        res = requests.get(url, headers=headers, params=payload)
        print(res.json())


if __name__ == "__main__":
    s = GetNewsData()
    s.get_naver_news_data()
