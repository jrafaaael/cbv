import { Hono } from "hono";
import { exchange } from "./exchange/exchange.routes";

const app = new Hono();

app.route("/", exchange);

export default app;
