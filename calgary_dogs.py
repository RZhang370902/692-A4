# calgary_dogs.py
# AUTHOR NAME Rick Zhang
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 README file.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import numpy as np
import pandas as pd

def main():

    # Import data here
    #all_data = pd.read_excel("WeatherData.xlsx", usecols = [2,5,6,7,8,9,10], index_col = [0,1,2,3])
    all_data = pd.read_excel("CalgaryDogBreeds.xlsx")
    print(type(all_data))

    

    dog = 'LABRADOR RETR'
    year = 2021
    x = all_data['Year'][all_data['Breed'] == dog]
    print(x)
    y = np.unique(x)
    print(y)

    z = np.array(all_data['Total'][(all_data['Breed'] == dog) & (all_data['Year'] == year)])
    print(z)
    print(np.sum(z))
    w = np.array(all_data['Total'][all_data['Year'] == year])
    print(np.sum(w))
    print(np.sum(z) / np.sum(w))
    print(all_data.isnull().any())


    print("ENSF 692 Dogs of Calgary")

    # User input stage

    # Data anaylsis stage

if __name__ == '__main__':
    main()
