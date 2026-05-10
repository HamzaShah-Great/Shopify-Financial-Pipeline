import pandas as pd
import matplotlib.pyplot as plt

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
# Creating the line Chart
Monthy_Revenue.plot(kind='line', marker='o', color='blue', figsize=(10,5))
plt.title("Monthly Gross Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Gross Revneue (€)")
plt.grid(True) 
#Export as an image to put in Excel Report
plt.tight_layout()
plt.savefig("revenue_trend.png")
print("Chart saved successfully as revenue_trend.png!")
# Creating a Summary Dictionary
summary_data = {
    "Metric" : ["Gross Revenue", "Refunded Value", "Refunded Rate", "Total COGS", "Net Revenue", "Net Profit", "Net Margin"],
    "Value" : [
        Total_Gross_Revenue,
        Total_Refunded_Value,
        f"{Refund_Rate_Percentage:.2f}%",
        Total_COGS_Value,
        Net_Revenue,
        Net_Profit,
        f"{Net_Margin:.2f}%"
    ]
}

# Converting it into a Pandas DataFrame
summary_df = pd.DataFrame(summary_data)
print("\nFinal Summary Table:")
print(summary_df)

# Exporting it into Excel
summary_df.to_excel('Financial_Report.xlsx',index=False)

# Formating and Polish of Report
from openpyxl.drawing.image import Image
# 1. Exporting the DataFrame to Excel, using the openpyxl engine
writer = pd.ExcelWriter('Financial_Report.xlsx', engine='openpyxl')
summary_df.to_excel(writer, sheet_name='Financial Summary', index=False)
# 2. Getting the specific worksheet so we can modify it
workbook = writer.book
worksheet = writer.sheets['Financial Summary']
# 3. Adjusting the column widths so the text isn't squished
worksheet.column_dimensions['A'].width = 20
worksheet.column_dimensions['B'].width = 20

# 4. Inserting the Matplotlib chart we saved earlier
# We load the image file, and put in excel(E2)
img = Image('revenue_trend.png')
worksheet.add_image(img, 'E2')

# 5. Saving the final Formatting workbook
writer.close()
print("Excel Report with Chart Generated Successfully!")

