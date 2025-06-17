

import pandas as pd

from io import StringIO

data = StringIO("""
Customer ID,Age,Gender,Purchase Amount (USD),Product Category,Purchase Date,Country,Payment Method
C001,25,Female,120.50,Electronics,2024-11-01,USA,Credit Card
C002,31,Male,75.00,Books,2024-11-02,Canada,PayPal
C003,22,Female,300.20,Fashion,2024-11-03,USA,Debit Card
C004,40,Male,450.00,Electronics,2024-11-05,UK,Credit Card
C005,29,Female,99.99,Cosmetics,2024-11-06,Germany,PayPal
C006,35,Male,149.90,Fashion,2024-11-07,Canada,Credit Card
C007,27,Female,199.00,Electronics,2024-11-08,USA,PayPal
C008,42,Male,85.75,Books,2024-11-09,France,Debit Card
C009,30,Female,210.40,Fashion,2024-11-10,UK,Credit Card
C010,50,Male,400.00,Electronics,2024-11-11,USA,Debit Card
""")

df = pd.read_csv(data)
df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])  # convert date
df.head()
print(df)