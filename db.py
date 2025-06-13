 # Conexión a PostgreSQL
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def insert_stock_data(data):
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
    )
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock_data (
            id SERIAL PRIMARY KEY,
            symbol TEXT,
            long_name TEXT,
            currency TEXT,
            regular_price REAL,
            previous_close REAL,
            open_price REAL,
            day_high REAL,
            day_low REAL,
            market_cap BIGINT,
            inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    cursor.execute("""
        INSERT INTO stock_data (
            symbol, long_name, currency, regular_price,
            previous_close, open_price, day_high, day_low, market_cap
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, (
        data['symbol'],
        data['long_name'],
        data['currency'],
        data['regular_price'],
        data['previous_close'],
        data['open_price'],
        data['day_high'],
        data['day_low'],
        data['market_cap']
    ))

    conn.commit()
    cursor.close()
    conn.close()
