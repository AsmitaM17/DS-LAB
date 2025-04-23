import pandas as pd
import matplotlib.pyplot as plt

# Sample data - replace this with your actual data
data = {
    'Year': [2020, 2020, 2021, 2021, 2022, 2022],
    'Product': ['A', 'B', 'A', 'C', 'B', 'D'],
    'Sales': [100, 150, 120, 80, 200, 90],
    'Price': [10, 15, 12, 8, 20, 9],
    'Region': ['North', 'South', 'East', 'West', 'North', 'South']
}

df = pd.DataFrame(data)
df['Revenue'] = df['Sales'] * df['Price']

# Set up the figure
plt.figure(figsize=(15, 4))

# 1. Top Products (Bar Chart)
plt.subplot(1, 3, 1)
df.groupby('Product')['Revenue'].sum().sort_values().plot(kind='barh', color='skyblue')
plt.title('Top Products by Revenue')
plt.xlabel('Total Revenue')

# 2. Region Comparison (Bar Chart)
plt.subplot(1, 3, 2)
df.groupby('Region')['Revenue'].sum().plot(kind='bar', color='lightgreen')
plt.title('Revenue by Region')
plt.ylabel('Total Revenue')

# 3. Yearly Trends (Line Chart)
plt.subplot(1, 3, 3)
df.groupby('Year')['Revenue'].sum().plot(marker='o', color='orange')
plt.title('Yearly Revenue Trend')
plt.ylabel('Revenue')

plt.tight_layout()
plt.show()