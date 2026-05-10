import pandas as pd

df = pd.read_csv("MOCK_DATA.csv", parse_dates=["order_date"])

#print(df.head())
#print()
#print(df.info()) 
df['Gross_Revenue'] = df['price'] * df['quantity']
print(df)
Total_Gross_Revenue = df['Gross_Revenue'].sum()
print(Total_Gross_Revenue)

refunded_orders = df[df['refund_status'] == 'refunded']

Total_Refunded_Value = refunded_orders['Gross_Revenue'].sum()

print(Total_Refunded_Value)

Refund_Rate_Percentage = (Total_Refunded_Value/Total_Gross_Revenue)*100
print(f"Over All Refund Rate : {Refund_Rate_Percentage:.2f}%")
