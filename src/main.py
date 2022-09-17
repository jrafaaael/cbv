import setup
from currencies import get_currencies
from database import db

if __name__ == "__main__":
    currencies = get_currencies()

    for code, value in currencies:
        currency_id = (
            db.table("currency").select("id").eq("iso_4217", code).execute()
        ).data[0]["id"]

        response = (
            db.table("exchange")
            .insert({"value": value, "symbol_id": currency_id})
            .execute()
        )
