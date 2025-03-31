CREATE TABLE trades (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10),
    price DECIMAL(10, 2),
    volume INT,
    timestamp TIMESTAMP DEFAULT NOW()
);
