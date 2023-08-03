import matplotlib.pyplot as plt

# Sample data for the line plot (replace with your actual temperature data)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature_values = [25, 26, 27, 28, 29, 30, 31, 30, 29, 28, 27, 26]

def create_temperature_line_plot(months, temperature_values):
    plt.figure(figsize=(10, 6))  # Optional: Set the figure size

    # Create the line plot for temperature
    plt.plot(months, temperature_values, marker='o', linestyle='-')

    # Customize the plot
    plt.title('Monthly Temperature Data')
    plt.xlabel('Month')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)

    # Display the plot
    plt.show()

# Call the function to generate the line plot for temperature
create_temperature_line_plot(months, temperature_values)
