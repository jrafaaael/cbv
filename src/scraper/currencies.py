import requests
from bs4 import BeautifulSoup as bs


class Currencies:
    URL = "http://www.bcv.org.ve/"

    def __scrape(self):
        page = requests.get(self.URL)
        soup = bs(page.content, "html.parser")
        dollar = soup.find("div", id="dolar")
        currencies_parent = dollar.parent
        currencies_wrapper = currencies_parent.find_all("div", recursive=False)
        return currencies_wrapper

    def __parse(self):
        container = self.__scrape()
        currencies = {}

        for currency_wrapper in container:
            code = currency_wrapper.find("span")
            value = currency_wrapper.find("strong")

            if code and value:
                currencies[code.text.strip()] = value.text.strip()

        return currencies

    def get(self):
        return self.__parse()
