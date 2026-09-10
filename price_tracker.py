import requests
from bs4 import BeautifulSoup

class Object:
    def __init__(self, name, target_price, url):
        self.name = name
        self.target_price = target_price
        self.url = url

    def check_if_reached_target(self):
        response = requests.get(self.url,timeout=10, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36", "Accept-Language": "en-US,en;q=0.9"})
        soup = BeautifulSoup(response.text, "html.parser")
        price_elem = soup.select_one("#corePrice_feature_div .a-price-whole")
        if price_elem:
            price = int(price_elem.text.split(".")[0].replace(",", ""))
            return price <= self.target_price
        return False

