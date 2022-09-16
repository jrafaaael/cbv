from currencies.scraper import Currencies

SYMBOLS = ["dolar", "euro", "yuan", "lira", "rublo"]

if __name__ == "__main__":
    page = Currencies().scrape()

    for symbol in SYMBOLS:
        currency = page.get(symbol).parse()
        print(currency)
