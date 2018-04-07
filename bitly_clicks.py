import sys
import requests
import urllib.parse
import json
import config

class BitlyApi():
    """bitly API にリクエストを送るクラス

    https://dev.bitly.com/get_started.html"""
    access_token = config.ACCESS_TOKEN
    base_url = "https://api-ssl.bitly.com"

    def get_link_lookup(self, long_url):
        """/v3/link/lookup へリクエストを行う"""
        # TODO urlは複数していできるっぽい
        path = "/v3/link/lookup"
        params = {
            "url": long_url,
            "access_token": self.access_token,
        }
        response = requests.get(
            self.base_url + path,
            params=params)
        return response.json()

    def get_link_clicks(self, link):
        """/v3/link/clicks へリクエストを行う"""
        path = "/v3/link/clicks"
        params = {
            "link": link,
            "access_token": self.access_token,
        }
        response = requests.get(
            self.base_url + path,
            params=params)
        return response.json()

    def get_link_encoders_count(self, link):
        path = "/v3/link/encoders_count"
        params = {
            "link": link,
            "access_token": self.access_token,
        }
        response = requests.get(
            self.base_url + path,
            params=params)
        return response.json()


if __name__ == "__main__":
    # loggingの設定をすることでrequestsの内容が見られる
    # import logging
    # logging.basicConfig(level=logging.DEBUG)
    long_url = sys.argv[1];
    api = BitlyApi()
    lookup_result = api.get_link_lookup(long_url)
    # print(result)
    short_link = lookup_result["data"]["link_lookup"][0]["aggregate_link"]
    clicks_result = api.get_link_clicks(short_link)
    # print(result)
    link_clicks = clicks_result["data"]["link_clicks"]
    encode_count_result = api.get_link_encoders_count(short_link)
    # print(encode_count_result)
    encode_count = encode_count_result["data"]["count"]
    print("URL: " + long_url)
    print("Clicks: " + str(link_clicks))
    print("Encode: " + str(encode_count))
