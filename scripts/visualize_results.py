import pandas as pd
import plotly.express as px

df = pd.read_csv('data/logistics_data_processed.csv')

summary = df.groupby('Carrier')[['Cost_USD', 'CO2_kg']].mean().reset_index()

fig = px.scatter(
    summary, 
    x="Cost_USD", 
    y="CO2_kg", 
    size="CO2_kg", 
    color="Carrier",
    text="Carrier",
    title="Logistics Efficiency: Average Cost vs. Carbon Footprint",
    labels={"Cost_USD": "Average Cost (USD)", "CO2_kg": "Average CO2 Emissions (kg)"}
)

fig.update_traces(textposition='top center')

fig.write_image("logistics_chart.png") 
fig.show()

print("✅ Success: 'logistics_chart.png' has been saved to your folder.")
