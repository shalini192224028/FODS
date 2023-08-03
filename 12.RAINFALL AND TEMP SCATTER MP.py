import matplotlib.pyplot as plt

# Sample data for the scatter plot (replace with your actual rainfall data)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall_values = [50, 40, 60, 80, 100, 120, 130, 120, 100, 80, 60, 50]

def create_rainfall_scatter_plot(months, rainfall_values):
    plt.figure(figsize=(10, 6))  # Optional: Set the figure size

    # Create the scatter plot for rainfall
    plt.scatter(months, rainfall_values, marker='o')

    # Customize the plot
    plt.title('Monthly Rainfall Data')
    plt.xlabel('Month')
    plt.ylabel('Rainfall (mm)')
    plt.grid(True)

    # Display the plot
    plt.show()

# Call the function to generate the scatter plot for rainfall
create_rainfall_scatter_plot(months, rainfall_values)
