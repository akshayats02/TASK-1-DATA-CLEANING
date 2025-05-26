import pandas as pd
df = pd.read_csv("C:/Users/hp/Downloads/archive/Mall_Customers.csv")
print(df.head())

selected_columns = ['CustomerID', 'Gender', 'Annual Income (k$)', 'Spending Score (1-100)']
df_selected = df[selected_columns]
print(df_selected.head())

print(df_selected.isnull().sum())
