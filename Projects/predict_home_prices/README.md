🏠 House Price Prediction using Linear Regression

📌 Overview

This project uses Linear Regression to model and predict house prices based on their size (in square feet).
The goal is to demonstrate how a simple machine learning model can be applied to real estate data to find trends and make predictions.

📂 Dataset

The dataset home_dataset.csv contains the following columns:

Column Name	Description
HouseSize	Size of the house in square feet
HousePrice	Price of the house in dollars

🛠 Steps Performed

Load Dataset

Read the CSV file into a Pandas DataFrame.

Data Visualization

Scatter plot of house size vs. price to visualize trends.

Data Splitting

Split into training and testing sets (80% train, 20% test).

Model Training

Train a LinearRegression model using scikit-learn.

Prediction & Evaluation

Predict house prices for the test set.

Compare actual vs. predicted prices visually.

Save Plots

Exported plots to plots/house_price.png and plots/house_price_prediction.png.

🚀 Requirements

Install dependencies with:

pip install numpy pandas scikit-learn matplotlib

▶️ How to Run

Place home_dataset.csv in the same folder as the script.

Run the script:

python house_price_prediction.py


Check the plots/ folder for the generated visualizations.

🔍 Key Insights

📈 There is a clear positive correlation between house size and price.

📊 A simple Linear Regression model can capture this trend effectively.

🎯 This approach can be extended to multiple features (location, bedrooms, etc.) for more accurate predictions.

📈 Skills Demonstrated

Data manipulation with Pandas

Data visualization with Matplotlib

Machine learning model training with scikit-learn

Train/test split and prediction evaluation

Saving plots programmatically