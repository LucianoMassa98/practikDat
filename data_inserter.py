import yfinance as yf
from db import insert_stock_data

def fetch_and_insert():
    ticker = 'AAPL'  # O el ticker que deseas automatizar
    stock = yf.Ticker(ticker)
    info = stock.info

    if not info:
        print(f"No se encontró información para {ticker}")
        return

    data = {
        'symbol': info.get("symbol"),
        'long_name': info.get("longName"),
        'currency': info.get("currency"),
        'regular_price': info.get("regularMarketPrice"),
        'previous_close': info.get("previousClose"),
        'open_price': info.get("open"),
        'day_high': info.get("dayHigh"),
        'day_low': info.get("dayLow"),
        'market_cap': info.get("marketCap"),
    }

    insert_stock_data(data)
    print(f"✅ Datos insertados para {ticker}")
