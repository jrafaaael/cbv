from typing import Text
import requests
from bs4 import BeautifulSoup as bs, Tag


class Currencies:
    __URL = "http://www.bcv.org.ve/"
    __CONVERTION_OFFSET = 1000000

    def __init__(self) -> None:
        self.__currency_wrapper = None
        self.__page = None

    def scrape(self):
        page = requests.get(self.__URL)
        soup = bs(page.content, "html.parser")

        self.__page = soup
        return self

    def get(self, id: Text = 'dolar'):
        page = self.__page

        if not (isinstance(page, bs)):
            raise Exception("You need scrape the page first")

        currency_wrapper = page.find("div", id=id)

        self.__currency_wrapper = currency_wrapper
        return self

    def parse(self):
        currency_wrapper = self.__currency_wrapper

        if not isinstance(currency_wrapper, Tag):
            raise Exception("Invalid element")

        code = currency_wrapper.find("span")
        value = currency_wrapper.find("strong")

        if not (code and value):
            raise Exception("Currency not found")

        code = code.text.strip()
        value = int(
            float(value.text.strip().replace(",", ".")) * self.__CONVERTION_OFFSET
        )

        return (code, value)
