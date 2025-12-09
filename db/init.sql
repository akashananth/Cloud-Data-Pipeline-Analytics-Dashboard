CREATE TABLE IF NOT EXISTS sales_raw (
    order_id        VARCHAR(50),
    order_date      DATE,
    customer_id     VARCHAR(50),
    product_id      VARCHAR(50),
    quantity        INTEGER,
    price           NUMERIC(10,2),
    country         VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS sales_daily (
    order_date      DATE PRIMARY KEY,
    total_revenue   NUMERIC(12,2),
    total_orders    INTEGER
);
