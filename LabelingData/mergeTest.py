import pandas as pd

# Create first data frame
df1 = pd.DataFrame({
   'key1': ['A', 'B', 'C', 'D'],
   'key2': ['W', 'X', 'Y', 'Z'],
   'value1': [1, 2, 3, 4],
   'value2': [5, 6, 7, 8]
})

# Create second data frame
df2 = pd.DataFrame({
   'key1': ['A', 'B', 'C', 'E'],
   'key2': ['W', 'X', 'Z', 'Y'],
   'value3': [9, 10, 11, 12],
   'value4': [13, 14, 15, 16]
})

merged_df = pd.merge(df1, df2, on=['key1', 'key2'], how='inner')

print(merged_df)