import { Hono } from "hono";

import { exchange as db } from "./exchange.database";

const exchange = new Hono();

exchange.get("/", (c) => {
  const lastUpdatedData = db.map((exchange) => ({
    ...exchange,
    rates: exchange.rates.at(-1),
  }));

  return c.json(lastUpdatedData);
});

export { exchange };
