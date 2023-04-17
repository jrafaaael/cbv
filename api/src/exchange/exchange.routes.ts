import { Hono } from "hono";
import {
  getExchangeRates,
  getExchangeRateByCurrencyNameOrId,
} from "./exchange.controller";

const exchange = new Hono();

exchange
  .get("/", getExchangeRates)
  .get("/:currencyNameOrId", getExchangeRateByCurrencyNameOrId);

export { exchange };
