import pandas as pd

# Sample data for the 'sales_data' DataFrame
data = {
    'product_name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product A'],
    'quantity_sold': [3, 2, 1, 4, 3, 2]
}

sales_data = pd.DataFrame(data)

# Now you can use the provided code snippet with the 'sales_data' DataFrame:
# Group the DataFrame by 'product_name' and sum the 'quantity_sold' for each product
product_sales_summary = sales_data.groupby('product_name')['quantity_sold'].sum()

# Sort the products based on the total quantity sold in descending order
sorted_product_sales = product_sales_summary.sort_values(ascending=False)

# Get the top 5 products that have been sold the most
top_5_products = sorted_product_sales.head(5)

print("Top 5 products sold the most in the past month:")
print(top_5_products)
