# Central Bank of Venezuela scraper and API

## Why?
Since some years ago, USD become the de-facto currency in venezuelan's day to day (more than venezuelan's Bolivar)

However, Central Bank of Venezuela (Banco Central de Venezuela or BCV) doesn't have an API (or another way) to programatically get official exchange rates

Since 2022, is needed that every commerce bill its products or services based on BCV USD instead of another exchange rates (knows as "Dólar paralelo"), so an API (or service) like this is needed

## Project structure
```
├── api/                     # cloudflare workers api build with hono
├── database/                # json file that works as db
├── scraper/                 # python script to scrape BCV webpage and store exchange rates
```

### Scraper
Built with python, beautifulsoup4 and requests

#### Install
```bash
# On project root
cd scraper
pip3 install -r requirements.txt
```

### API
Built with nodejs, cloudflare workers, wrangler and hono

#### Install
```bash
# On project root
cd api
npm install
```

## To-do
- [ ] Get value by date from API (query params)
