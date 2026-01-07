import pandas as pd

df = pd.read_csv('data/logistics_data_raw.csv')

median_cost = df['Cost_USD'].median()
df['Cost_USD'] = df['Cost_USD'].fillna(median_cost)

df = df[df['Weight_KG'] > 0]

conditions = [
    (df['Carrier'] == 'Air-Express'),
    (df['Carrier'] == 'Ocean-Freight'),
    (df['Carrier'] == 'Ground-Truck'),
    (df['Carrier'] == 'Rail-Link')
]
values = [0.50, 0.01, 0.11, 0.03] 

import numpy as np
df['Emission_Factor'] = np.select(conditions, values)

df['CO2_kg'] = (df['Weight_KG'] / 1000) * df['Distance_KM'] * df['Emission_Factor']

df.to_csv('data/logistics_data_processed.csv', index=False)

print("✅ Success: Cleaned data and CO2 calculations saved to 'data/logistics_data_processed.csv'.")
print(df[['Carrier', 'CO2_kg']].groupby('Carrier').mean())
