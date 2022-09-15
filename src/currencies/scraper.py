from typing import Dict, List
import requests
from bs4 import BeautifulSoup as bs


class Currencies:
    __URL = "http://www.bcv.org.ve/"
    __CONVERTION_OFFSET = 1000000

    def __scrape(self):
        page = requests.get(self.__URL)
        soup = bs(page.content, "html.parser")
        dollar = soup.find("div", id="dolar")
        currencies_parent = dollar.parent
        currencies_wrapper = currencies_parent.find_all("div", recursive=False)
        return currencies_wrapper

    def __parse(self) -> List[Dict[str, int]]:
        container = self.__scrape()
        currencies = []

        for currency_wrapper in container:
            code = currency_wrapper.find("span")
            value = currency_wrapper.find("strong")

            if code and value:
                code = code.text.strip()
                value = int(
                    float(value.text.strip().replace(",", "."))
                    * self.__CONVERTION_OFFSET
                )
                currencies.append({code: value})

        return currencies

    def get(self) -> List[Dict[str, int]]:
        return self.__parse()
