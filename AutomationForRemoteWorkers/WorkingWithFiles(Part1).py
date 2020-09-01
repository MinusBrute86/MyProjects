import os  # Gives access to .listdir method

data_location ='C:/Users/{USER}/Documents/'   # Path we want to go through
file_list = []  # Declares/Makes an empty list
for file in os.listdir(data_location):  # For each file in path
    file_list.append(file)  # Aggregates each file in path into empty list

print(file_list)