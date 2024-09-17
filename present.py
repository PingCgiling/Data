import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('flight_prices.csv')

# Display the first few rows of the DataFrame
print(df.head(10))

# summary statistics  columns
print("Summary statistics:")
print(df.describe())

#ALL THE NEXT CODE ITS REFERING TO OPEN POP UP SCHEMAS


# distribution of flight prices
plt.figure(figsize=(8, 4)) # Parameters for the schema window 
plt.hist(df['Value'], bins=25, edgecolor='black') #bins - its colums 25 its the number of them edge colour changing the colour of them
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Distribution of Flight Prices')
plt.show()

# flight prices over time
plt.figure(figsize=(8, 4))
df.set_index('Depart Date', inplace=True)
df['Value'].plot(kind='line')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Flight Prices Over Time')
plt.show()
