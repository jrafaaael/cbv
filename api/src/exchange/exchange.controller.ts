import { Context, Env } from "hono";
import { exchange as db } from "./exchange.database";

const CONVERTION_OFFSET = 1000000;

export function getExchangeRates(c: Context<Env, "/", {}>) {
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
}

export function getExchangeRateByCurrencyNameOrId(
  c: Context<Env, "/:currencyNameOrId", {}>
) {
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
}
