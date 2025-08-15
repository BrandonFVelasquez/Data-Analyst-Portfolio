import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Read the dataset from csv file
data = pd.read_csv('home_dataset.csv')

#extract features and target variable
house_sizes = data['HouseSize'].values
house_prices = data['HousePrice'].values

# Visualize the data
plt.scatter(house_sizes, house_prices, marker ='o', color ='blue')
plt.title('House Prices vs. House Size')
plt.xlabel('House Size (sq.ft)')
plt.ylabel('House Price ($)')
plt.show()
plt.savefig('plots/house_price.png')

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(house_sizes, house_prices, test_size=0.2, random_state=42)

# Reshape the data to be 2D arrays
X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Visualize the results
plt.scatter(X_test, y_test, marker='o', color='blue', label='Actual Prices')
plt.plot(X_test, predictions, color='red', linewidth=2, label='Predicted Prices')
plt.xlabel('House Size (sq ft)')
plt.ylabel('House Price (Millions $)')
plt.title('House Size vs Price')
plt.legend()
plt.show()

# Export the plot as an image file
plt.savefig('plots/house_price_prediction.png')
