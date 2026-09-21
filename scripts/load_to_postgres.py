import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv("../Data/Cleaned/amazon_sales_cleaned.csv")

engine = create_engine("postgresql://postgres:300704@localhost:5432/db_analyst_project")


df.to_sql("amazon_sales", engine, if_exists="replace", index=False)

print("✅ Data berhasil dimasukkan ke tabel 'amazon_sales' di PostgreSQL")