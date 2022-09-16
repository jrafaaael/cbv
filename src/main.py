from currencies.scraper import Currencies
from constants.currencies import SYMBOLS

if __name__ == "__main__":
    page = Currencies().scrape()

    for symbol in SYMBOLS:
        code, value = page.get(symbol).parse()
        print(code, value)
