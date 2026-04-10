import pandas as pd

with open("pandas_foundation\\input.csv", mode='r') as f:
    data = pd.read_csv(f)


# print(data[data['Port'] == 80])

# print(data[(data['Port'] == 80) | (data['Months'] == "Feb")])

# print(data[data['Port'].isin([22,80,443])])

# print(data[data['Months'].notnull()])

# data['Risk'] = data['Port'] > 100
# print(data)

# print(data['Port'].unique())

# print(data['Port'].value_counts())

print(data['Port'].describe())