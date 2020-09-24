import quandl
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

# Pass API key
quandl.ApiConfig.api_key = "WGsWx6BJAygpVtUqycFt"

# Get Stock Data
df = quandl.get('WIKI/AMZN')

# Take a look at data
# print(df.head())

# Get Adj. Close Price
df = df[['Adj. Close']]

# Take a look at new data for Adj. Close
# print(df.head())

# Variable for forecasting 'n' days out into the future
forecast_out = 30

# Create another df column / Shifted 'n' units up
df['Prediction'] = df[['Adj. Close']].shift(-forecast_out)

# Print new data set
# print(df.tail())

### Create independent data set (X) ###
# Convert df to a numpy array
X = np.array(df.drop(['Prediction'], 1))

# Remove the last 'n' rows
X = X[:-forecast_out]
# print(X)

### Create the dependent data set (Y) ###
# Convert df to a numpy array / Give all values including NaN's
Y = np.array(df['Prediction'])

# Get all Y values except last 'n' rows/days
Y = Y[:-forecast_out]
# print(Y)

### Split data into 80% Training and 20% Testing ###
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

# Create and train the Support Vector Machine (Regressor)
svm_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svm_rbf.fit(x_train, y_train)

# Testing Model: Score / Returns coefficient of determination R^2 of the prediction
# Best possible score is 1.0
svm_confidence = svm_rbf.score(x_test, y_test)
print("SVM Confidence:", svm_confidence)

# Create and train the Linear Regression Model
linear = LinearRegression()
linear.fit(x_train, y_train)

# Testing Linear Regression Model: Score / Returns coefficient of determination R^2 of the prediction
# Best possible score is 1.0
linear_confidence = linear.score(x_test, y_test)
print("Linear Confidence:", linear_confidence)

# Set x_forecast equal to last 30 rows of original data set from Adj. Close column
x_forecast = np.array(df.drop(['Prediction'], 1))[-forecast_out:]
# print(x_forecast)

# Print the predictions for the next 'n' days using Support Vector Machine
svm_prediction = svm_rbf.predict(x_forecast)
print("\nSVM Prediction:\n", svm_prediction)

# Print the predictions for the next 'n' days using Linear Regression Model
linear_prediction = linear.predict(x_forecast)
print("\nLinear Prediction:\n", linear_prediction)