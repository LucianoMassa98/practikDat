from fastapi import FastAPI, HTTPException
import yfinance as yf

app = FastAPI(title="Yahoo Finance API Wrapper")

@app.get("/stock/{ticker}")
def get_stock_info(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        if not info:
            raise HTTPException(status_code=404, detail="Stock not found")

        return {
            "symbol": info.get("symbol"),
            "longName": info.get("longName"),
            "currency": info.get("currency"),
            "regularMarketPrice": info.get("regularMarketPrice"),
            "previousClose": info.get("previousClose"),
            "open": info.get("open"),
            "dayHigh": info.get("dayHigh"),
            "dayLow": info.get("dayLow"),
            "marketCap": info.get("marketCap"),
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
