from fastapi import FastAPI
import asyncpg
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

app = FastAPI()

async def connect_db():
    return await asyncpg.connect(DATABASE_URL)

@app.get("/")
async def root():
    return {"message": "Trading SaaS API is running!"}

@app.get("/trades")
async def get_trades():
    try:
        conn = await connect_db()
        trades = await conn.fetch("SELECT * FROM trades;")
        await conn.close()
        return trades
    except Exception as e:
        return {"error": str(e)}

@app.post("/trades")
async def add_trade(trade: dict):
    try:
        conn = await connect_db()
        query = "INSERT INTO trades (symbol, price, volume) VALUES ($1, $2, $3) RETURNING *"
        result = await conn.fetchrow(query, trade["symbol"], trade["price"], trade["volume"])
        await conn.close()
        return {"message": "Trade added!", "trade": result}
    except Exception as e:
        return {"error": str(e)}
