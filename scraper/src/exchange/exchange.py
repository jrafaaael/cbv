import requests
from bs4 import BeautifulSoup as bs, ResultSet, Tag


__URL = "https://www.bcv.org.ve/"


def __scrape():
    page = requests.get(__URL, verify=False)
    soup = bs(page.content, "html.parser")

    return soup


def get_exchanges():
    page = __scrape()
    exchanges_wrapper: ResultSet[Tag] = page.find_all("div", class_="row recuadrotsmc")
    exchanges = [
        (
            code.text.strip(),
            float(value.text.strip().replace(",", ".")),
            name["id"],
        )
        for wrapper in exchanges_wrapper
        if (code := wrapper.find("span"))
        and (value := wrapper.find("strong"))
        and (name := wrapper.find_parent("div", id=True))
    ]

    return exchanges
