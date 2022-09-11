from scraper.currencies import Currencies

if __name__ == "__main__":
    currencies = Currencies().get()

    print(currencies)
