"""
Stock Analysis of Adani Ports

This script performs a complete analysis of Adani Ports stock data.
It loads the data from a CSV, cleans it, engineers key financial features,
creates visualizations, and exports the final, analysis-ready dataset.
"""

# 1. SETUP
# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. DATA LOADING AND CLEANING
print("Loading and cleaning data...")

# Load the dataset from the CSV file
df = pd.read_csv("ADANIPORTS.csv")

# Slim down the dataframe to only the columns we actually need for the analysis
essential_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
df = df[essential_columns]

# Convert the 'Date' column from a string to a proper datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Set the date column as the index for easier plotting and data selection
df.set_index('Date', inplace=True)

print("Data cleaning complete.")


# 3. FEATURE ENGINEERING
# Create new columns based on the existing data to add more analytical value
print("Engineering new features...")

# Calculate the daily return as a percentage
df['Daily_Return'] = df['Close'].pct_change() * 100

# Add 50-day and 200-day moving averages to identify trends
df['MA50'] = df['Close'].rolling(window=50).mean()
df['MA200'] = df['Close'].rolling(window=200).mean()

# Calculate the 50-day rolling volatility to measure risk
df['Volatility'] = df['Daily_Return'].rolling(window=50).std()

# The rolling calculations create empty values at the start, so we drop them
df.dropna(inplace=True)

print("Feature engineering complete.")


# 4. DATA VISUALIZATION
# Create plots to visually inspect the data and trends.
# NOTE: Each plot will open in a new window. You must close the window for the script to continue.
print("Creating visualizations...")

# Set a clean, professional style for the charts
plt.style.use('fivethirtyeight')

# Plot 1: Price trend against the moving averages
plt.figure(figsize=(14, 7))
plt.plot(df['Close'], label='Close Price', color='blue', alpha=0.6) # CORRECTED: 'Close' and alpha
plt.plot(df['MA50'], label='50-Day Moving Average', color='orange')  # CORRECTED: 'label'
plt.plot(df['MA200'], label='200-Day Moving Average', color='red') # CORRECTED: 'label'
plt.title('Adani Ports: Price Trend Analysis')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.show()

# Plot 2: Histogram of daily returns to visualize volatility
plt.figure(figsize=(12, 6))
sns.histplot(df['Daily_Return'], kde=True, bins=50)
plt.title('Adani Ports: Volatility (Distribution of Daily Returns)')
plt.xlabel('Daily Return (%)')
plt.ylabel('Frequency')
plt.show()


# 5. EXPORT THE FINAL DATASET
# Save the final, enriched dataframe to a new CSV file
df.to_csv('ADANIPORTS_Analyzed.csv')

print("\nAnalysis complete. 'ADANIPORTS_Analyzed.csv' has been saved.")