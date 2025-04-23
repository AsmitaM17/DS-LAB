import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample data generation (replace with actual data)
np.random.seed(42)
years = [2020, 2021, 2022, 2023]
products = ['A', 'B', 'C', 'D', 'E', 'F']
regions = ['North', 'South', 'East', 'West']

# Create a DataFrame with random sales data
data = {
    'Year': np.random.choice(years, 100),
    'Product': np.random.choice(products, 100),
    'Sales': np.random.randint(50, 500, 100),
    'Price': np.random.uniform(10, 100, 100).round(2),
    'Region': np.random.choice(regions, 100)
}

df = pd.DataFrame(data)
df['Revenue'] = df['Sales'] * df['Price']

# 1. Top Performing Products (Bar Graph)
plt.figure(figsize=(10, 6))
top_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
top_products.plot(kind='bar', color='skyblue')
plt.title('Top Performing Products by Revenue')
plt.xlabel('Product')
plt.ylabel('Total Revenue ($)')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--')
plt.show()

# 2. Region-wise Revenue Comparison (Pie Chart & Bar Graph)
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
region_revenue = df.groupby('Region')['Revenue'].sum()
region_revenue.plot(kind='pie', autopct='%1.1f%%', colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Region-wise Revenue Share')

plt.subplot(1, 2, 2)
region_revenue.plot(kind='bar', color='orange')
plt.title('Region-wise Revenue Comparison')
plt.xlabel('Region')
plt.ylabel('Total Revenue ($)')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()

# 3. Yearly Trends (Line Plot)
plt.figure(figsize=(10, 6))
yearly_trend = df.groupby(['Year', 'Product'])['Revenue'].sum().unstack()
yearly_trend.plot(marker='o')
plt.title('Yearly Sales Trends by Product')
plt.xlabel('Year')
plt.ylabel('Revenue ($)')
plt.grid(True, linestyle='--')
plt.legend(title='Product')
plt.show()