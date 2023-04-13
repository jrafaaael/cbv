from exchange import get_exchanges
from database import Database
from datetime import datetime, timezone

CONVERTION_OFFSET = 1000000

if __name__ == "__main__":
    db = Database("exchanges")
    exchanges = get_exchanges()
    now = datetime.now(timezone.utc).isoformat()

    for code, value, name in exchanges:
        currency = db.find(field="id", value=code)

        if not currency:
            currency = db.create({"id": code, "name": name, "rates": []})

        if (
            len(currency["rates"]) == 0
            or not currency["rates"][-1]["value"] == value
        ):
            db.update(
                "rates",
                {"value": int(value * CONVERTION_OFFSET), "updated_at": now},
                where={"field": "id", "value": code},
            )
