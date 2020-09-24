# Simple Machine Learning Program
from sklearn.linear_model import LinearRegression
from random import randint
from tqdm.auto import tqdm

# Create Two Empty Lists
feature_set = []  # data set for 'x'/'input data'
target_set = []  # data set for 'y'/'output data'

# Get number of rows for data set
number_of_sets = 5

# Limit the possible values in the data set
random_number_limit = 10

# Create randint for Coefficients
coefficient_x = randint(0, 10)
coefficient_y = randint(0, 10)
coefficient_z = randint(0, 10)

# Create the data set
# Create feature data set
for set in tqdm(range(0, number_of_sets)):  # For each set of (x, y, z) in "number_of_sets"
    x = randint(0, random_number_limit)  # Column
    y = randint(0, random_number_limit)  # Column
    z = randint(0, random_number_limit)  # Column

    # Create linear function for target data set
    function = (coefficient_x*x) + (coefficient_y*y) + (coefficient_z*z)
    feature_set.append([x, y, z])
    target_set.append(function)

# Create Linear Regression Model
model = LinearRegression()
model.fit(feature_set, target_set)

# Print for loop parts
print('Actual Set Data:')
print('Coefficients Used: ' + '[' + str(coefficient_x) + ', ' + str(coefficient_y) + ', ' + str(coefficient_z) + ']')
print('Feature Set List (Input): ' + str(feature_set))
print('Target Set List (Output): ' + str(target_set))