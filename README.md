End-to-end data analyst portfolio project: cleaning, analyzing, and visualizing Amazon e-commerce sales data using Python, PostgreSQL, and Power BI.

## 📊 Project Overview
This project analyzes ~128,000 Amazon sales transaction records to uncover business insights on sales performance, regional distribution, cancellation rates, and the impact of promotions.

## 🗂️ Data Source
Dataset: [Amazon Sale Report (Kaggle)](https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data)  
Note: Raw data files are not included in this repo due to size; cleaned dataset is available in `Data/Cleaned/`.

## 🛠️ Tools & Tech Stack
- **Python** (pandas) — data cleaning and transformation
- **PostgreSQL** — database storage and SQL analysis
- **Power BI** — interactive dashboard and visualization

## 🔄 Workflow
1. **Data Exploration** — inspected 7 raw CSV files for missing values, duplicates, and data types (`notebooks/01_explore.py`)
2. **Data Cleaning** — handled missing values, standardized column names, converted date formats (`scripts/clean_amazon_sales.py`)
3. **Database Loading** — loaded cleaned data into PostgreSQL (`scripts/load_to_postgres.py`)
4. **SQL Analysis** — explored business questions using SQL queries (category performance, cancellation rates, regional sales, promotion impact)
5. **Dashboard** — built an interactive 2-page dashboard in Power BI (`POWER BI VISUAL/`)

## 📈 Key Insights
- **Set** and **kurta** are the top-selling categories, together contributing over 55% of total sales
- Sales peaked in March 2022 and declined steadily through June 2022
- **Maharashtra** leads regional sales, followed by Karnataka and Telangana
- 14.2% of orders were cancelled; Set and kurta categories show the highest cancellation rates
- Orders using promotions generated **2.5x more volume** and slightly higher average order value than non-promoted orders
- The business is **99.3% B2C**, with B2B transactions being negligible in volume
- **Size M** is the most frequently ordered size across all product categories

## 📊 Dashboard Preview
<img width="1919" height="1032" alt="SALES OVERVIEW" src="https://github.com/user-attachments/assets/7e192078-715e-4ee0-9023-e100051f8667" />
<img width="1435" height="804" alt="Order   Customer Insights" src="https://github.com/user-attachments/assets/984ccf96-b633-44ce-aa96-66bce7ebce90" />

## 📁 Repository Structure
```
├── Data/
│   └── Cleaned/          # Cleaned dataset (CSV)
├── notebooks/            # Data exploration scripts
├── scripts/              # Cleaning & database loading scripts
├── POWER BI VISUAL/      # Power BI dashboard file (.pbix)
└── README.md
```

## 👤 Author
**Kevin Yosia**  
Information Systems Graduate 
