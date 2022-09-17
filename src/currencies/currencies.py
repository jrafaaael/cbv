# import os
import requests
from bs4 import BeautifulSoup as bs, ResultSet, Tag


__URL = "http://www.bcv.org.ve/"
__CONVERTION_OFFSET = 1000000


def __scrape():
    page = requests.get(__URL)
    soup = bs(page.content, "html.parser")

    return soup


def get_currencies():
    page = __scrape()
    currencies_wrapper: ResultSet[Tag] = page.find_all("div", class_="row recuadrotsmc")
    currencies = [
        (
            code.text.strip(),
            int(float(value.text.strip().replace(",", ".")) * __CONVERTION_OFFSET),
        )
        for wrapper in currencies_wrapper
        if (code := wrapper.find("span")) and (value := wrapper.find("strong"))
    ]

    return currencies
