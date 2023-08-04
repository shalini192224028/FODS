import pandas as pd

# Sample customer data with age and purchase information
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Age': [25, 32, 45, 28, 38, 22, 35, 40, 50, 28],
    'PurchaseMade': ['2023-07-10', '2023-07-25', '2023-06-15', '2023-07-05', '2023-07-12', '2023-07-18', '2023-06-30', '2023-07-20', '2023-07-02', '2023-07-27']
}

# Convert the data dictionary to a DataFrame
df = pd.DataFrame(data)

# Convert 'PurchaseMade' column to pandas datetime format
df['PurchaseMade'] = pd.to_datetime(df['PurchaseMade'])

# Calculate the date of one month ago from the current date
one_month_ago = pd.Timestamp.now() - pd.DateOffset(months=1)

# Filter data to include only customers who made a purchase in the past month
df_past_month = df[df['PurchaseMade'] >= one_month_ago]

# Calculate the frequency distribution of ages
age_frequency = df_past_month['Age'].value_counts()

print(age_frequency)
