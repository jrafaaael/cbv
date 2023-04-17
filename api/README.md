# Central Bank of Venezuela API

Built with nodejs and hono. Deployed on cloudflare workers

## Commands
**Run these commands inside `api/` folder**
| Command          | Action                                                                     |
| :--------------- | :------------------------------------------------------------------------- |
| `npm install`    | Install deps                                                               |
| `npm run start`  | Starts local dev server                                                    |
| `npm run deploy` | Deploy API in cloudflare workers (you must need to be auth with wrangler)  |
| `npm run test`   | 😅                                                                         |

## API endpoints
GET `/`: Return latest update of exchange rates

GET `/:currencyIdOrName`: Return latest update of exchange rates given a currency ID or name