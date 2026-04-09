import pandas as pd

# list_data = [1,2,3,4,5]
# series_data = pd.Series(list_data)
# print(series_data)

# dict_data = {'Yes': [50,21], 'No':[131,2]}
# data = pd.DataFrame(dict_data,index=['ProductA','ProductB'])
# data.to_csv("pandas_foundation\\basic_table.csv")

data = pd.read_csv("pandas_foundation\\input.csv")
print(data)
print(data.shape)
print(data.head())
print(data.info())