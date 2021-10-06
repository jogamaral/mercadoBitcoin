DROP TABLE IF EXISTS coin.cripto;
DROP SCHEMA IF EXISTS coin;
CREATE SCHEMA coin;
CREATE TABLE coin.cripto (
    token VARCHAR(50),
    high NUMERIC(16,8),
    low NUMERIC(16,8),
    vol NUMERIC(16,8),
    last_price NUMERIC(16,8),
    buy_price NUMERIC(16,8),
    sell_price NUMERIC(16,8),
    open_price NUMERIC(16,8),
    unix_time BIGINT,
    utc_timestamp TIMESTAMP
);