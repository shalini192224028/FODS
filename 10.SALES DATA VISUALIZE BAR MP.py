import matplotlib.pyplot as plt

# Assuming you have the monthly sales data in two lists: months and sales_values
# months = ['Jan', 'Feb', 'Mar', ...]
# sales_values = [1000, 1500, 1200, ...]

def create_bar_plot(months, sales_values):
    plt.figure(figsize=(10, 6))  # Optional: Set the figure size

    # Create the bar plot
    plt.bar(months, sales_values)

    # Customize the plot
    plt.title('Monthly Sales Data')
    plt.xlabel('Month')
    plt.ylabel('Sales Value')
    plt.grid(True)

    # Display the plot
    plt.show()

# Example usage:
# Replace 'months' and 'sales_values' with your actual data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales_values = [1000, 1500, 1200, 1800, 2000, 1600]
create_bar_plot(months, sales_values)
