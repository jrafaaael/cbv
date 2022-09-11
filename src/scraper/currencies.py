from typing import Dict
import requests
from bs4 import BeautifulSoup as bs


class Currencies:
    __URL = "http://www.bcv.org.ve/"

    def __scrape(self):
        page = requests.get(self.__URL)
        soup = bs(page.content, "html.parser")
        dollar = soup.find("div", id="dolar")
        currencies_parent = dollar.parent
        currencies_wrapper = currencies_parent.find_all("div", recursive=False)
        return currencies_wrapper

    def __parse(self) -> Dict[str, float]:
        container = self.__scrape()
        currencies = {}

        for currency_wrapper in container:
            code = currency_wrapper.find("span")
            value = currency_wrapper.find("strong")

            if code and value:
                code = code.text.strip()
                value = int(float(value.text.strip().replace(",", ".")) * 1000000)
                currencies[code] = value

        return currencies

    def get(self) -> Dict[str, float]:
        return self.__parse()
