# Cloud-Data-Pipeline-Analytics-Dashboard

An end-to-end cloud-style **data engineering and analytics pipeline** built using Docker, FastAPI, PostgreSQL, Python ETL, and Power BI.
This project analyzes retail sales and **detects suspicious transactions** using a scalable microservices architecture — suitable for real-world production environments.

## Project Architecture
Jupyter ETL ---> PostgreSQL (Docker) <--- FastAPI API (Docker)
▲ │
└──── Power BI Dashboard ───┘


## Objectives

- Ingest raw sales transaction data
- Build analytics tables for KPIs
- Expose insights via REST API
- Create interactive Power BI dashboard for business users
- Detect abnormal/suspicious activities in sales

This project demonstrates how organizations monitor performance using KPI dashboards.
The same pipeline structure can be applied to digital marketing and campaign analytics,
where KPIs such as revenue, growth, top performers, and anomaly detection help stakeholders
optimize performance and identify risks.

The dashboard is designed to support:
- Performance monitoring using KPIs and trends  
- Ranking top performers (similar to top channels or campaigns)  
- Detecting abnormal patterns or unusual activity  
- Management-ready reporting for decision-makers

## Tech Stack

| Layer | Technology |
|------|------------|
| Database | PostgreSQL (Docker) |
| Backend | FastAPI + Uvicorn (Docker) |
| ETL | Python (Pandas + Psycopg2) |
| Orchestration | Docker Compose |
| Visualization | Power BI |
| Version Control | Git + GitHub |


## 🔄 Data Pipeline Flow

1️⃣ Load CSV data into Jupyter Notebook  
2️⃣ ETL → Insert into PostgreSQL (`sales_raw_kaggle`)  
3️⃣ Create aggregated table (`sales_by_salesperson`)  
4️⃣ FastAPI exposes analytics endpoints  
5️⃣ Power BI connects to Postgres → Dashboard visualizes insights  


## API Endpoints (FastAPI)

Open interactive docs:

 `http://localhost:8000/docs`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | API health check |
| GET | `/kpi/top-salespeople?limit=10` | Top performers ranked by revenue |
| GET | `/kpi/suspicious-summary` | Count of suspicious activities |
| GET | `/salesperson/{id}` | Detailed view per salesperson |

<img width="1541" height="773" alt="Sales Analytics API -Swagger UI" src="https://github.com/user-attachments/assets/7ab2e54d-e9b5-4a25-87a5-313397bc9cb8" />

## 📂 Project Structure
Cloud_Data_Pipeline_Analytics_Dashboard/
│
├─ api/
│ ├─ main.py
│ └─ requirements.txt
│
├─ etl/
│ └─ 01_etl.ipynb
│
├─ db/
│ └─ init.sql
│
├─ data/
│ └─ sales_raw.csv (not included due to size)
│
├─ powerbi_dashboard/
│ └─ Sales_Analytics_Dashboard.png
│
├─ docker-compose.yml
└─ README.md

## Run With Docker

```bash
docker-compose up --build

API will be available at:
http://localhost:8000

Power BI Connection

| Setting  | Value       |
| -------- | ----------- |
| Server   | `localhost` |
| Port     | `5432`      |
| Database | `salesdb`   |
| User     | `postgres`  |
| Password | `postgres`  |

Power BI Connection

Dashboard Highlights

✔ Top salespeople by revenue
✔ Suspicious transaction distribution
✔ KPI metrics for executives
✔ Interactive slicers for drill-down analysis

 Key Insights

- A small number of top performers contribute a large share of total revenue, highlighting where performance is concentrated.
- The anomaly view helps identify unusual transaction patterns that may require further investigation.
- KPI trends provide a quick overview of performance health and changes over time.
- Interactive filters allow drill-down analysis for deeper performance evaluation.


Real-World Skills Demonstrated

✔ Data ingestion and transformation
✔ SQL data modeling
✔ REST API development
✔ Containerization with Docker
✔ BI reporting & stakeholder insights
✔ GitHub portfolio project delivery

