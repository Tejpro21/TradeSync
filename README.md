# Trading SaaS Tool

A simple trading journal SaaS tool built with FastAPI and PostgreSQL.

## Features
- Log trades with price, volume, and symbol
- Retrieve trade history
- Hosted with Render/Supabase

## Setup
1. Clone this repo  
2. Install dependencies: `pip install -r requirements.txt`  
3. Create a `.env` file with your database credentials  
4. Run: `uvicorn main:app --host 0.0.0.0 --port 8000`
