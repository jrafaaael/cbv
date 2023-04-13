import { Hono } from "hono";

import { exchange as db } from "./exchange.database";

const exchange = new Hono();
const CONVERTION_OFFSET = 1000000;

exchange
  .get("/", (c) => {
    const lastUpdatedData = db.map((exchange) => {
      const { rates, ...rest } = exchange;
      const lastRate = rates.at(-1);

      return {
        ...rest,
        rate: {
          ...lastRate,
          value: (lastRate?.value ?? 0) / CONVERTION_OFFSET,
        },
      };
    });

    return c.json(lastUpdatedData);
  })
  .get("/:currencyNameOrId", (c) => {
    const currencyNameOrId = c.req.param("currencyNameOrId");
    const currency = db.find(
      (exchange) =>
        exchange.id.toLowerCase() === currencyNameOrId.toLowerCase() ||
        exchange.name.toLowerCase() === currencyNameOrId.toLowerCase()
    );

    if (!currency) {
      return c.json({ message: "Currency not found" }, 404);
    }

    const { rates, ...rest } = currency;
    const lastRate = rates.at(-1);

    return c.json({
      ...rest,
      rate: {
        ...lastRate,
        value: (lastRate?.value ?? 0) / CONVERTION_OFFSET,
      },
    });
  });

export { exchange };
