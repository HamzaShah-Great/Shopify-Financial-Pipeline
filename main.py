import pandas as pd

df = pd.read_csv("MOCK_DATA.csv", parse_dates=["order_date"])

print(df.head())
print()
print(df.info()) 