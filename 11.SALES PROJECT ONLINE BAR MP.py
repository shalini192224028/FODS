import matplotlib.pyplot as plt

# Sample data for the bar plot
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales_values = [1000, 1500, 1200, 1800, 2000, 1600]

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

# Call the function to generate the bar plot
create_bar_plot(months, sales_values)
