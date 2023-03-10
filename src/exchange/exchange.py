import requests
from bs4 import BeautifulSoup as bs, ResultSet, Tag
import os


__URL = "https://www.bcv.org.ve/"
__CONVERTION_OFFSET = 1000000


def __scrape():
    # page = requests.get(__URL, verify=False)
    # soup = bs(page.content, "html.parser")

    with open(f"{os.getcwd()}/bcv.html") as p:
        page = p.read()

    soup = bs(page, "html.parser")

    return soup


def get_exchanges():
    page = __scrape()
    exchanges_wrapper: ResultSet[Tag] = page.find_all("div", class_="row recuadrotsmc")
    exchanges = [
        (
            code.text.strip(),
            int(float(value.text.strip().replace(",", ".")) * __CONVERTION_OFFSET),
            name["id"],
        )
        for wrapper in exchanges_wrapper
        if (code := wrapper.find("span"))
        and (value := wrapper.find("strong"))
        and (name := wrapper.find_parent("div", id=True))
    ]

    return exchanges
