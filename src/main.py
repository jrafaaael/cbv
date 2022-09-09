import requests
from bs4 import BeautifulSoup as bs


def main():
    URL = "http://www.bcv.org.ve/"
    page = requests.get(URL)
    soup = bs(page.content, "html.parser")
    dollar = soup.find("div", id="dolar")
    currencies_container = dollar.parent
    currencies = currencies_container.find_all("div", recursive=False)

    for currency in currencies:
        code = currency.find("span")
        value = currency.find("strong")

        if not code or not value:
            continue

        print(code.text.strip())
        print(value.text.strip())
        print()


if __name__ == "__main__":
    main()
