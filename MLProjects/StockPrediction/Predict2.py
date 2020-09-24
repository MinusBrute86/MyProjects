# Import Packages

from yahoo_fin.stock_info import *
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

# ----------------------------------------------------------------------------------------------------------------------

# pd.set_option('display.max_columns', None)

# ----------------------------------------------------------------------------------------------------------------------

# Get Stock Data
ticker = input("Enter Stock Ticker: ")
df = get_data(ticker)
# print(df.tail())

# ----------------------------------------------------------------------------------------------------------------------

# Get Adj. Close Price data
df = df[['open']]
# print(df.tail())

# ----------------------------------------------------------------------------------------------------------------------

# Variable for forecasting 'n' days out into the future
forecast_out = 5

# ----------------------------------------------------------------------------------------------------------------------

# Create another df column / Shifted 'n' units up
df['Prediction'] = df[['open']].shift(-forecast_out)
# print(df.tail())

# ----------------------------------------------------------------------------------------------------------------------

# Create independent data set (X)
# Convert df to a numpy array
X = np.array(df.drop(['Prediction'], 1))

# ----------------------------------------------------------------------------------------------------------------------

# Remove the last 'n' rows
X = X[:-forecast_out]
# print(X)

# ----------------------------------------------------------------------------------------------------------------------

# Create the dependent data set (Y)
# Convert df to a numpy array / Give all values including NaN's
y = np.array(df['Prediction'])

# ----------------------------------------------------------------------------------------------------------------------

# Get all Y values except last 'n' rows/days
y = y[:-forecast_out]
# print(y)

# ----------------------------------------------------------------------------------------------------------------------

# Split data into 80% Training and 20% Testing
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# ----------------------------------------------------------------------------------------------------------------------

# Create and train the Support Vector Machine (Regressor)
svm_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svm_rbf.fit(x_train, y_train)

# ----------------------------------------------------------------------------------------------------------------------

# Set x_forecast equal to last 30 rows of original data set from Adj. Close column
x_forecast = np.array(df.drop(['Prediction'], 1))[-forecast_out:]
# print(x_forecast)

# ----------------------------------------------------------------------------------------------------------------------

# Testing Model: Score / Returns coefficient of determination R^2 of the prediction
# Best possible score is 1.0
svm_confidence = svm_rbf.score(x_test, y_test)
print("SVM Confidence:", svm_confidence)

# ----------------------------------------------------------------------------------------------------------------------

# Print the predictions for the next 'n' days using Support Vector Machine
svm_prediction = svm_rbf.predict(x_forecast)
print("SVM Prediction:\n", svm_prediction)

# ----------------------------------------------------------------------------------------------------------------------

# Create and train the Linear Regression Model
linear = LinearRegression()
linear.fit(x_train, y_train)

# ----------------------------------------------------------------------------------------------------------------------

# Testing Linear Regression Model: Score / Returns coefficient of determination R^2 of the prediction
# Best possible score is 1.0
linear_confidence = linear.score(x_test, y_test)
print("\nLinear Confidence:", linear_confidence)

# ----------------------------------------------------------------------------------------------------------------------

# Print the predictions for the next 'n' days using Linear Regression Model
linear_prediction = linear.predict(x_forecast)
print("Linear Prediction:\n", linear_prediction)