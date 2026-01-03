import pandas as pd
import numpy as np
import os

# Create the data
rows = 1000
data = {
    'OrderID': range(1001, 1001 + rows),
    'Carrier': np.random.choice(['Air-Express', 'Ocean-Freight', 'Ground-Truck', 'Rail-Link'], rows),
    'Origin': np.random.choice(['New York', 'London', 'Shanghai', 'Singapore'], rows),
    'Distance_KM': np.random.randint(100, 15000, rows),
    'Weight_KG': np.random.uniform(5, 5000, rows),
    'Cost_USD': np.random.uniform(100, 8000, rows),
}

df = pd.DataFrame(data)

# Inject errors for the "Cleaning" phase
df.iloc[0:10, 5] = np.nan # Missing costs
df.iloc[20:25, 4] = -99   # Impossible weights

# Ensure the data folder exists and save
os.makedirs('data', exist_ok=True)
df.to_csv('data/logistics_data_raw.csv', index=False)

print("✅ Success: 'data/logistics_data_raw.csv' created.")