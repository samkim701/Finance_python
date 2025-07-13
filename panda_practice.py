import pandas as pd
#series
values = [10, 20, 30, 40, 50]
s = pd.Series(values, index=['a', 'b', 'c', 'd', 'a'])
print(s.loc['a'])

#Data Frame
df = pd.DataFrame({
    'name': ['Mike', 'Bob', 'Alice'],
    'age': [30, 80, 45],
    'job': ['Programmer', 'Clerk', 'Designer']
})
print(df)
df = df.set_index('name')
print(df)

df1 = pd.DataFrame({
    'a': [1,2,3]
}, index = [0,1,2])

df2 = pd.DataFrame({
    'a': [10,20,30]
}, index = [1,2,0])

print(df1)
print(df2)
print(df1*df2)

df = df.reset_index()
print(df) 
df.to_csv('mydata.csv', index=None)
print(pd.read_csv('mydata.csv'))
print(pd.read_csv('mydata.csv', index_col=0))
df.to_json('mydata.json')
print(df.to_dict())
