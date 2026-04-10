import pandas as pd

with open("pandas_foundation\\input.csv",mode='r') as f:
    data =pd.read_csv(f)

# print(data['Months'][0])

# print(data.iloc[0])
# print(data.iloc[0,2])
# print(data.iloc[:,2])
# print(data.iloc[[5,7],2])
# print(data.iloc[-5:])

# print(data.loc[0,'Months'])
# print(data.loc[:,['Months','Port']])

# print(data.iloc[0:5])
# print(data.loc[0:5])

# data_new = data.set_index("Alphabets")
# print(data_new.head())

