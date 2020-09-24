import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

data = pd.read_csv("student-mat.csv", sep=";")
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

# ----------------------------------------------------------------------------------------------------------------------

"""best_score = 0
for score in range(100000):
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

    linear = LinearRegression()
    linear.fit(x_train, y_train)
    linear_confidence = linear.score(x_test, y_test)  # 1.0 is best score
    # print("Confidence:", linear_confidence)

    if linear_confidence > best_score:
        best_score = linear_confidence
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f)"""

# ----------------------------------------------------------------------------------------------------------------------

pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)

# coefficients = linear.coef_
# intercept = linear.intercept_
x_test_predict = linear.predict(x_test)

for i in range(len(x_test_predict)):
    print("Prediction:", x_test_predict[i], "Inputs:", x_test[i], "Output:", y_test[i])

# ----------------------------------------------------------------------------------------------------------------------
# Using MatPlotLib

p = "absences"
style.use("ggplot")
pyplot.scatter(data[p], data[predict])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()
