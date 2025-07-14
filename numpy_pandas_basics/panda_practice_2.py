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
df1.loc['Alice'] = [75, 'Clerk'] #value 변경
df1.loc['John'] = [90, 'Teacher']
print(df1)
print(df1.iloc[:, 1])
print(df1.age ** 2)
print(df1)

#Functions
def myfunction(x):
    if x % 3 == 0:
        return x ** 2
    else:
        return x // 2
print(df1.age.apply(myfunction)) ##apply function
def myfunction2(x):
    if x.endswith('r'):
        return 'Without Job'
    else:
        return x
print(df1.job.apply(myfunction2))
df1.job = df1.job.apply(myfunction2)
df1['summary'] = df1.apply(lambda row: f'Age: {row["age"]}, Job: {row["job"]}', axis = 1)
print(df1)  
df1.at['Alice', 'age'] = float('nan')
df1.at['Bob', 'job'] = None
print(df1)
#df.dropna() #drops the na
#df.fillna(int) #fills the na with designed number
for i, row in df1.iterrows():
    print(row['summary'])  ##iterrate
for i, col in df1.items():
    print(col['Alice'])
print(df1)
print(df1.age > 50)
print((df1.age > 50) & (df1.job.notna()))
df1 = df1.reset_index()
print(df1)
df1.loc[df1['name'] == 'Alice', 'job' ]= 'Without Job'
df1['summary'] = df1.apply(lambda row: f'Age: {row["age"]}, Job: {row["job"]}', axis=1)
df1.age = df1.age.fillna(33.0)
print(df1)

import datetime as dt
df1['birthday'] = df1['age'].apply(lambda x: dt.datetime.now() - dt.timedelta(days=365*x))
#설명: age그룹 value들을 꺼내서, 모든 value들에게 lambda를 적용시킨다(함수). 그 value들을
#birthday라는 그룹을 새로 만들어 넣는다.)
print(df1)
print(df1[df1.birthday.dt.year > 1950])
ages = [30, 90]
print(df1[df1.age.isin(ages)])
print(df1.query('age > 30')) #numexpr
df1.at[2, 'job'] = 'Programmer' #value 변경 예시 1
df1.loc[df1['name'] == 'Bob', 'job'] = 'Programmer'
print(df1)
df1 = df1.drop('summary', axis = 1)
print(df1)
print(df1.groupby('job').agg({   #aggregates and averages by job
    'age': 'mean'
}))
df1.loc[4] = {
    'name': 'Jane',
    'age': 35,
    'job': 'Programmer',
    'summary': None  # or create a real summary string if you want
}
print(df1.groupby('job').agg({   #aggregates and averages by job
    'age': ['mean', 'min', 'max', 'sum']
}))
print(df1.sort_values('age'))

##merging

df2 = pd.DataFrame({
    'Item' : ['A', 'B', 'C'],
    'Price' : [10, 20, 30]
})
df3 = pd.DataFrame({
    'Item' : ['D', 'E', 'F'],
    'Price' : [40, 50, 60]
})
print(pd.concat([df2, df3]).reset_index().drop('index', axis = 1))

df4 = pd.DataFrame({
    'Item' : ['A', 'B', 'C'],
    'Price' : [10, 20, 30]
})
df5 = pd.DataFrame({
    'Country' : ['X', 'Y', 'Z'],
    'Available' : [True, True, False]
})
print(pd.concat([df4, df5], axis =1)) 

df6 = pd.DataFrame({
    'Item' : ['B', 'C', 'D'],
    'Country' : ['X', 'Y', 'Z']
})

print(pd.merge(df4, df6)) #common merge
print(pd.merge(df4, df6, how='outer')) #outer merge

