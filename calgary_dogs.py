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

# Additional functions

def find_breed_in_years(dog_breed, all_data):
    """find_breed_in_years: Print in which years the dog breed is found

    Args:
        dog_breed (str): string represents breed of the dog
        all_data (pandas dataframe): data frame created from CalgaryDogBreeds.xlsx

    Returns: 
        unique_year_output (numpy.ndarray): numpy array of years in which the dog breed is found
    """

    # Filter out rows of 'Year' where 'Breed' value is user's input
    breed_find_in_year = all_data['Year'][all_data['Breed'] == dog_breed]
    # Reduce filtered result to unique values. e.g [2021, 2022, 2022, 2022] -> [2021, 2022]
    unique_year_output = np.unique(breed_find_in_year)
    # Convert Reduced result to string
    year_output_string = " ".join(str(x) for x in unique_year_output)
    print("The", dog_breed, "was found in the top breeds for years: ", year_output_string)
    return unique_year_output


def find_total_registered(dog_breed, all_data):
    """find_total_registered: calculate and display total number of registry of the inputed dog breed across all years

    Args:
        dog_breed (str): string represents breed of the dog
        all_data (pandas dataframe): data frame created from CalgaryDogBreeds.xlsx

    Returns:
        None
    """

    # Filter 'Total' value by 'Breed' then sum up
    total_registered = np.sum(all_data['Total'][all_data['Breed'] == dog_breed])
    # Display total numer of registry
    print("There have been", total_registered, dog_breed, "dogs registered total.")


def find_total_registered_mi(dog_breed, multi_index_all_data):
    """find_total_registered: calculate and display total number of registry of the inputed dog breed across all years

    Args:
        dog_breed (str): string represents breed of the dog
        all_data (pandas multi-index dataframe): data frame created from CalgaryDogBreeds.xlsx

    Returns:
        None
    """
    # Group and sum total by breed
    df = multi_index_all_data.groupby('Breed')['Total'].sum()
    total_registered = df.loc[dog_breed]
    # Display total numer of registry
    print("There have been", total_registered, dog_breed, "dogs registered total.")
    

def percentage_registered_in_year(dog_breed, year, all_data):
    """percentage_registered_in_year: for the input dog breed, calculate registry% over all breeds in a single input year

    Args:
        dog_breed (str): string represents breed of the dog
        year (int): int represents a year
        all_data (pandas dataframe): data frame created from CalgaryDogBreeds.xlsx

    Returns:
        percent (float): registry% over all breeds in the input year
    """

    total = np.sum(all_data['Total'][all_data['Year'] == year])
    dog = np.sum(all_data['Total'][(all_data['Breed'] == dog_breed) & (all_data['Year'] == year)])
    if total > 0:
        percentage = dog / total
    else: percentage = 0
    return percentage


def percentage_top_breeds_over_year(dog_breed, years, all_data):
    """percentage_top_breeds_over_year: for the input dog breed, calculate registry% over all breeds for each single year

    Args:
        dog_breed (str): string represents breed of the dog
        years (int): numpy array of years in which the dog breed is found
        all_data (pandas dataframe): data frame created from CalgaryDogBreeds.xlsx

    Returns:
        None
    """

    # for the input dog breed, calculate and display registry% over all breeds for each single year
    for i in years:
        percentage = percentage_registered_in_year(dog_breed, i, all_data)
        print("The ", dog_breed, " was ", f"{percentage:.6%}", " of top breeds in ", i, ".", sep="")


def percentage_top_breeds_all_year(dog_breed, years, all_data):
    """percentage_top_breeds_all_year: for the input dog breed, calculate registry% over all breeds among all input years

    Args:
        dog_breed (str): string represents breed of the dog
        years (numpy.ndarray): numpy array of years in which the dog breed is found
        all_data (pandas dataframe): data frame created from CalgaryDogBreeds.xlsx

    Returns:
        None
    """
    total = 0
    dog = 0
    for i in years: #For all input years
        # Add up number of registry for all dog over all years
        total += np.sum(all_data['Total'][all_data['Year'] == i])
        # Add up number of registry for the input dog breed over all years
        dog += np.sum(all_data['Total'][(all_data['Breed'] == dog_breed) & (all_data['Year'] == i)])
    # Calculate input breed / all breed %
    percentage = dog/total
    # Display the result
    print("The", dog_breed, "was", f"{percentage:.6%}", " of top breeds across all years.")


def percentage_top_breeds_all_year_mi(dog_breed, years, multi_index_all_data):
    """percentage_top_breeds_all_year: for the input dog breed, calculate registry% over all breeds among all input years

    Args:
        dog_breed (str): string represents breed of the dog
        years (numpy.ndarray): numpy array of years in which the dog breed is found
        all_data (pandas dataframe): data frame created from CalgaryDogBreeds.xlsx

    Returns:
        None
    """
    total = 0
    dog = 0
    for i in years: #For all input years
        a = multi_index_all_data.loc[i]
        b = a.groupby('Breed')['Total'].sum()
        # Add up number of registry for all dog over all years
        dog += b.loc[dog_breed]
        total += np.sum(b)
        # Add up number of registry for the input dog breed over all years
        #dog += np.sum(all_data['Total'][(all_data['Breed'] == dog_breed) & (all_data['Year'] == i)])
    # Calculate input breed / all breed %
    percentage = dog/total
    # Display the result
    print("The", dog_breed, "was", f"{percentage:.6%}", " of top breeds across all years.")



def percentage_breeds_month(dog_breed, month, year, all_data):
    """percentage_breeds_month: calculate and return registry% of input dog breed over all dog breed for the input month and year

    Args:
        dog_breed (str): string represents breed of the dog
        month (int): int represents the month
        years (numpy.ndarray): numpy array of years in which the dog breed is found
        all_data (pandas dataframe): data frame created from CalgaryDogBreeds.xlsx

    Returns:
        percentage (float): registry% of input dog breed over all dog breed for the input month and year

    """

    total = np.sum(all_data['Total'][(all_data['Year'] == year) & (all_data['Month'] == month)])
    dog = np.sum(all_data['Total'][(all_data['Breed'] == dog_breed) & (all_data['Year'] == year) & (all_data['Month'] == month)])
    if total > 0:
        percentage = dog / total
    else: percentage = 0
    return percentage


def most_popular_month(dog_breed, all_data):
    """most_popular_month: find and display the month appears most for the registry of a dog breed

    Args:
        dog_breed (str): string represents breed of the dog
        all_data (pandas dataframe): data frame created from CalgaryDogBreeds.xlsx

    Returns:
        None
    """

    # Filter 'Month Value' by dog breed
    a = pd.DataFrame(all_data['Month'][all_data['Breed'] == dog_breed])
    # Count frequency of each month
    count_freq = dict(a['Month'].value_counts())
    a['count_freq'] = a['Month']
    a['count_freq'] = a['count_freq'].map(count_freq)
    # Filter out month with highest frequency
    b = a['Month'][a.count_freq >= a['count_freq'].max()]
    # Reduce to unique month value
    b = b.unique()
    # Print result
    print("Most popular month(s) for ", dog_breed, ": ", " ".join(str(x) for x in b), sep="")


def most_popular_year_month(dog_breed, years, all_data):
    """most_popular_year_month: find the month that has highest number of registry of the dog breed in all input years

    Args:
        dog_breed (str): string represents breed of the dog
        years (numpy.ndarray): numpy array of years in which the dog breed is found
        all_data (pandas dataframe): data frame created from CalgaryDogBreeds.xlsx

    Returns:
        None
    """

    for i in years: # do calculation for all years
        # Filter 'Total' by finding the max value
        df = all_data[(all_data['Breed'] == dog_breed) & (all_data['Year'] == i)]
        df_2 = df[df['Total'] == df['Total'].max()]
        # Print 'Month' values where total is the max over the year.
        print("Most popular month(s) for ", dog_breed, " in ", i, " : ", " ".join(str(x) for x in df_2['Month']), sep="")

# Main loop

def main():

    # Import data here
    #all_data = pd.read_excel("CalgaryDogBreeds.xlsx")
    multi_index_all_data = pd.read_excel("CalgaryDogBreeds.xlsx", usecols = [0,1,2,3], index_col=[0, 2])
    #some operation is easier after reset index
    all_data = multi_index_all_data.reset_index()

    breed_found = False

    # User input stage 

    # Sample input: 'LABRADOR RETR'

    # Take user input and convert all char to capital.
    # If user input is not found, ask user to try again until a valid input is detected.

    print("\n 692-A4 Calgary Dogs \n")
    while (not breed_found):
        user_input = input("Please enter a breed: ")
        user_input = user_input.upper()
        breed_found = all_data['Breed'].isin([user_input]).any().any()
        try:
            if (not breed_found):
                raise ValueError()
            else: dog_breed = user_input
        except ValueError:
            print("Dog breed not found in the data. Please try again.")
   
    print("You have entered", dog_breed)

    # Analysis stage
    year_breed_found = find_breed_in_years(dog_breed, all_data)

    # find_total_registered(dog_breed, all_data)
    # Version using multi-index
    find_total_registered_mi(dog_breed, multi_index_all_data)

    percentage_top_breeds_over_year(dog_breed, year_breed_found, all_data)

    # percentage_top_breeds_all_year(dog_breed, year_breed_found, all_data)
    # Version using multi-index
    percentage_top_breeds_all_year_mi(dog_breed, year_breed_found, multi_index_all_data)
        
    most_popular_month(dog_breed, all_data)

    most_popular_year_month(dog_breed, year_breed_found, all_data)

    print("\n Program Ends \n")


if __name__ == '__main__':
    main()
