import setup
from currencies import get_currencies

if __name__ == "__main__":
    currencies = get_currencies()

    for code, value in currencies:
