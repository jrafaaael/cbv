from currencies.scraper import Currencies
from currencies.names import CURRENCY_NAMES
import setup

if __name__ == "__main__":
    page = Currencies().scrape()

    for currency_name in CURRENCY_NAMES:
        code, value = page.get(currency_name).parse()
        print(currency_name, code, value)
