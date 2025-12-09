from fastapi import FastAPI, HTTPException
from typing import Optional
import os
import psycopg2
from psycopg2.extras import RealDictCursor

# === Database configuration ===
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = "salesdb"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_PORT = "5432"


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT,
    )


# === FastAPI app ===
app = FastAPI(
    title="Sales Analytics API",
    description="API exposing KPIs from Kaggle sales dataset",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/kpi/top-salespeople")
def top_salespeople(limit: int = 10):
    """
    Top N salespeople by total_sales from sales_by_salesperson table
    """
    query = """
        SELECT
            salesperson_id,
            total_quantity,
            total_sales,
            num_transactions,
            num_suspicious
        FROM sales_by_salesperson
        ORDER BY total_sales DESC
        LIMIT %s;
    """
    try:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, (limit,))
                rows = cur.fetchall()
        return rows
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/kpi/suspicious-summary")
def suspicious_summary():
    """
    Summary of suspicious vs non-suspicious transactions from sales_raw_kaggle
    """
    query = """
        SELECT
            suspicious,
            COUNT(*) AS count_transactions,
            SUM(total_sales) AS total_sales
        FROM sales_raw_kaggle
        GROUP BY suspicious
        ORDER BY count_transactions DESC;
    """
    try:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query)
                rows = cur.fetchall()
        return rows
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/salesperson/{salesperson_id}")
def salesperson_detail(salesperson_id: str):
    """
    Detailed metrics for one salesperson:
    total sales, quantity, num transactions, suspicious count + raw tx count
    """
    agg_query = """
        SELECT
            salesperson_id,
            total_quantity,
            total_sales,
            num_transactions,
            num_suspicious
        FROM sales_by_salesperson
        WHERE salesperson_id = %s;
    """

    tx_query = """
        SELECT
            COUNT(*) AS raw_transactions
        FROM sales_raw_kaggle
        WHERE salesperson_id = %s;
    """

    try:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(agg_query, (salesperson_id,))
                agg_row = cur.fetchone()

                if not agg_row:
                    raise HTTPException(status_code=404, detail="Salesperson not found")

                cur.execute(tx_query, (salesperson_id,))
                tx_row = cur.fetchone()

        agg_row["raw_transactions"] = tx_row["raw_transactions"]
        return agg_row

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
