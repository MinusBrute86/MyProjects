import os  # Gives access to .listdir method
import pandas as pd  # Pass data to DataFrame (like excel)
from datetime import date  # Imports date

data_location = 'C:/Users/{USER}}/Documents/'  # Path we want to go through
file_list = []  # Declares/Makes an empty list
for file in os.listdir(data_location):  # For each file in path
    file_list.append(file)  # Aggregates each file in path into empty list

data = {'file_names' : file_list}  # Creates file with stored info from above
file_df = pd.DataFrame(data)  # Passes data to DataFrame
new_file_directory = 'C:/Users/{USER}/Documents/PythonAutomationTesting/'  # Define new directory
today = date.today()  # Calls current date
file_df.to_csv(new_file_directory + 'PythonDocTest - ' + str(today) + '.txt')  # Used .to_csv because I don't have Excel, but creates text file with directory data