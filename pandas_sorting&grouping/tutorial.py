import pandas as pd

with open("pandas_sorting&grouping\\input.csv",mode='r') as f:
    data=pd.read_csv(f)

# new_data = data.sort_values(by='Failures')

# print(data.sort_values(by='Failures', ascending=False))

# print(data.sort_values(by=['Failures','Port']))

# print(data.groupby('User').count())

# print(data.groupby('User')['Failures'].agg(['count','sum','mean']))

# print(data.groupby('User')['Failures'].sum().sort_values(ascending=False))