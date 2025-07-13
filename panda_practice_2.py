import pandas as pd 
from sklearn.datasets import fetch_california_housing
df = fetch_california_housing(as_frame=True).frame
print(df)
print(df.head(10))
print(df.tail)
#pd.options.display.max_columns = 5
print(df['HouseAge'].count())
print(df['HouseAge'].sum())
import matplotlib.pyplot as plt
print(df['HouseAge'].hist())
plt.title('House Age')
plt.show() #Shows in jupitar notebook
plt.savefig("house_age_histogram.png") #Or do this

import yfinance as yf
stock_df = yf.download('AAPL')
print(stock_df)
stock_df.Close.plot()
plt.savefig("stock.png")

df1 = pd.DataFrame({
    'name': ['Mike', 'Alice', 'Bob'],
    'age': [30, 45, 80],
    'job': ['Programmer', 'Designer', 'Accountant']
})
df1 = df1.set_index('name')
print(df1)
print(df1.loc['Alice', 'age'])
print(df1.iloc[2, 0])
df1.at['Alice', 'age'] = 60
df1.loc['Alice'] = [75, 'Clerk']
df1.loc['John'] = [90, 'Teacher']
print(df1)
print(df1.iloc[:, 1])
print(df1.age ** 2)
print(df1)
