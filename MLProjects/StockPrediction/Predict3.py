# Import Packages

from yahoo_fin.stock_info import *
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
from tqdm.auto import tqdm

# ----------------------------------------------------------------------------------------------------------------------


class DataFrame:

    def __init__(self):
        self.ticker = input("Enter Stock Ticker: ")
        self.df = get_data(self.ticker)
        self.column = 'adjclose'
        self.predict = 'Prediction'
        self.forecast_out = 5
        self.linear_score = 0
        self.linear = LinearRegression()

    def start(self):
        print("Current Price:", get_live_price(self.ticker))
        print("\n" + str(self.df.tail(1)) + "\n")

        # Get column Price data
        self.df = self.df[[self.column]]

        # Create another df column / Shifted 'n' units up
        self.df[self.predict] = self.df[[self.column]].shift(-self.forecast_out)

        # Numpy Array Conversion / Remove the last 'n' rows
        self.X = np.array(self.df.drop([self.predict], 1))
        self.X = self.X[:-self.forecast_out]

        # Numpy Array Conversion / Remove the last 'n' rows
        self.y = np.array(self.df.drop([self.predict], 1))
        self.y = self.y[:-self.forecast_out]

        # Split data into 90% Training and 10% Testing
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.1)

        # Looping for Best Score
        for score in tqdm(range(100000)):
            self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.1)

            # Linear Training/Testing
            self.linear = LinearRegression()
            self.linear.fit(self.x_train, self.y_train.ravel())
            self.linear_confidence = self.linear.score(self.x_test, self.y_test)

            if self.linear_confidence > self.linear_score:
                self.linear_score = self.linear_confidence
                with open("Predict3linearmodel.pickle", "wb") as file:
                    pickle.dump(self.linear, file)

        # Open Pickle File
        read_linear_pickle = open("Predict3linearmodel.pickle", "rb")
        self.linear = pickle.load(read_linear_pickle)
        self.linear_confidence = self.linear.score(self.x_test, self.y_test)

        # Set x_forecast equal to last 'n' rows of original data set from column
        self.x_forecast = np.array(self.df.drop([self.predict], 1))[-self.forecast_out:]

        # Print the predictions for the next 'n' days using Linear Regression Model
        print("Linear Confidence:", self.linear_confidence)
        self.linear_prediction = self.linear.predict(self.x_forecast)
        print("Linear Prediction:", self.linear_prediction)


DF = DataFrame()
DF.start()