import pandas as pd
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("../Data/Raw/Amazon Sale Report.csv", low_memory=False)

df = df.drop(columns=["Unnamed: 22", "index"])

df.columns = df.columns.str.lower().str.replace(" ", "_").str.replace("-", "_")

df["date"] = pd.to_datetime(df["date"], format="%m-%d-%y")

df["has_promotion"] = df["promotion_ids"].notna()
df = df.drop(columns=["promotion_ids"])

df["fulfilled_by"] = df["fulfilled_by"].fillna("Unknown")

df["courier_status"] = df["courier_status"].fillna("Not Available")

df = df.dropna(subset=["ship_city", "ship_state", "ship_postal_code", "ship_country"])

df["amount"] = df["amount"].fillna(0)
df["currency"] = df["currency"].fillna("INR")  # asumsikan currency default


print("Shape akhir:", df.shape)
print()
print("Missing values setelah cleaning:")
print(df.isnull().sum())

df.to_csv("../Data/Cleaned/amazon_sales_cleaned.csv", index=False)
print("\n✅ Tersimpan di Data/Cleaned/amazon_sales_cleaned.csv")