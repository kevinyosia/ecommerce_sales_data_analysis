import pandas as pd
import warnings
warnings.filterwarnings('ignore')

path = "../Data/Raw/"

files = {
    "amazon_sales": "Amazon Sale Report.csv",
    "sale_report": "Sale Report.csv",
    "international_sales": "International sale Report.csv",
    "may_2022": "May-2022.csv",
    "pl_march_2021": "P  L March 2021.csv",
    "expense_iigf": "Expense IIGF.csv",
    "cloud_warehouse": "Cloud Warehouse Compersion Chart.csv",
}

dfs = {}
for key, filename in files.items():
    try:
        df = pd.read_csv(path + filename, low_memory=False)
        dfs[key] = df
        print(f"✅ {key}: {df.shape}")
    except Exception as e:
        print(f"❌ {key}: ERROR - {e}")


print("\n=== AMAZON SALES ===")
df_main = dfs["amazon_sales"]
print(df_main.dtypes)
print()
print("Missing values:")
print(df_main.isnull().sum())
print()
print("Duplicate rows:", df_main.duplicated().sum())
print()
print(df_main.head(3).to_string())