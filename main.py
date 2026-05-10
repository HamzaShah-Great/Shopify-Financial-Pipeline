import pandas as pd


df = pd.read_csv("MOCK_DATA.csv", parse_dates=["order_date"])
df = df.dropna(subset=['order_id'])

#print(df.head())
#print()
#print(df.info()) 

#Gross Revenue
df['Gross_Revenue'] = df['price'] * df['quantity'] 
print(df)
Total_Gross_Revenue = df['Gross_Revenue'].sum()
print(Total_Gross_Revenue)
#Refund Value
refunded_orders = df[df['refund_status'] == 'refunded'] 
Total_Refunded_Value = refunded_orders['Gross_Revenue'].sum() 
print(Total_Refunded_Value)
#Refund Rate
Refund_Rate_Percentage = (Total_Refunded_Value/Total_Gross_Revenue)*100
print(f"Over All Refund Rate : {Refund_Rate_Percentage:.2f}%")
#Cost of Goods Sold
df['Total_COGS'] = df['cogs'] * df['quantity']
Total_COGS_Value = df['Total_COGS'].sum()
print(f"Total COGS : {Total_COGS_Value:.3f}")
#Net Revenue
Net_Revenue = Total_Gross_Revenue - Total_Refunded_Value
print(f"Net Revenue : {Net_Revenue}")
#Net Profit
Net_Profit = Net_Revenue - Total_COGS_Value
print(f"Net Profit : {Net_Profit:.2f}")
#Net Margin
Net_Margin = (Net_Profit/Net_Revenue) * 100
print(f"Net Margin Percentage : {Net_Margin:.2f}")
#Month Over Month Growth
df["Year_Month"] = df['order_date'].dt.to_period('M')
Monthy_Revenue = df.groupby('Year_Month')['Gross_Revenue'].sum()
print(Monthy_Revenue)
mom_growth = Monthy_Revenue.pct_change() *100
print("Month-Over-Month Growth:")
print(mom_growth)