import matplotlib.pyplot as plt

# Sample data for the line plot
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales_values = [1000, 1500, 1200, 1800, 2000, 1600]

# Create the line plot
plt.figure(figsize=(10, 6))  # Optional: Set the figure size
plt.plot(months, sales_values, marker='o', linestyle='-')

# Customize the plot
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales Value')
plt.grid(True)

# Display the plot
plt.show()
