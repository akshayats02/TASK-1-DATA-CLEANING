df_selected['Gender'] = df_selected['Gender'].str.lower().replace({'male': 'm', 'female': 'f'})
print(df_selected['Gender'].unique())
