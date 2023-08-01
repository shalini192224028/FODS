import numpy as np

# Assuming house_data is your NumPy array containing the house dataset.
# Replace this with your actual data.
house_data = np.array([
    [4, 2000, 250000],
    [5, 2400, 300000],
    [3, 1800, 200000],
    [5, 2800, 350000],
    # ... more data
])

# Step 2: Filter rows where the number of bedrooms is greater than four
bedrooms_greater_than_four = house_data[house_data[:, 0] > 4]

# Step 3: Extract the sale price column from the filtered rows
sale_prices = bedrooms_greater_than_four[:, 2]

# Step 4: Calculate the average sale price
average_sale_price = np.mean(sale_prices)

print(f"The average sale price of houses with more than four bedrooms is: {average_sale_price}")
