import sys
import requests
import urllib.parse
import json
import logging
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


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    long_url = sys.argv[1];
    # print("check url: " + long_url)
    api = BitlyApi()
    # print("link lookup")
    result = api.get_link_lookup(long_url)
    # print(result)
    short_link = result["data"]["link_lookup"][0]["aggregate_link"]
    # print("short link: " + short_link)
    result = api.get_link_clicks(short_link)
    # print(result)
    link_clicks = result["data"]["link_clicks"]
    print("Link clicks: " + str(link_clicks))
