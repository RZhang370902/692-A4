import pandas as pd
import numpy as np

user_input = 'LABRADOR RETR'

all_data = pd.read_excel("CalgaryDogBreeds.xlsx")

def take_user_input():
    userinput = input("Please enter a do breed: ")
    userinput = userinput.upper()
    return userinput

def find_breed_in_years(dog_breed):
    breed_find_in_year = all_data['Year'][all_data['Breed'] == dog_breed]
    unique_year_output = np.unique(breed_find_in_year)
    year_output_string = " ".join(str(x) for x in unique_year_output)
    print("The", dog_breed, "was found in the top breeds for years: ", year_output_string)
    return unique_year_output

def find_total_registered(dog_breed):
    total_registered = np.sum(all_data['Total'][all_data['Breed'] == dog_breed])
    print("There have been", total_registered, dog_breed, "dogs registered total.")

def percentage_registered_in_year(dog_breed, year):
    total = np.sum(all_data['Total'][all_data['Year'] == year])
    dog = np.sum(all_data['Total'][(all_data['Breed'] == dog_breed) & (all_data['Year'] == year)])
    percentage = dog / total
    return percentage

def percentage_top_breeds_over_year(dog_breed, years):
    for i in years:
        percentage = percentage_registered_in_year(dog_breed, i)
        print("The ", dog_breed, " was ", f"{percentage:.6%}", " of top breeds in ", i, ".", sep="")

def percentage_top_breeds_all_year(dog_breed, years):
    total = 0
    dog = 0
    for i in years:
        total += np.sum(all_data['Total'][all_data['Year'] == i])
        dog += np.sum(all_data['Total'][(all_data['Breed'] == dog_breed) & (all_data['Year'] == i)])
    percentage = dog/total
    print("The", dog_breed, "was", f"{percentage:.6%}", " of top breeds across all years.")

def percentage_breeds_month(dog_breed, month, year):
    total = np.sum(all_data['Total'][(all_data['Year'] == year) & (all_data['Month'] == month)])
    dog = np.sum(all_data['Total'][(all_data['Breed'] == dog_breed) & (all_data['Year'] == year)])
    if total > 0:
        percentage = dog / total
    else: percentage = 0
    return percentage
  


    


a = pd.DataFrame(all_data['Month'][all_data['Breed'] == user_input])

print(a)
print(a.size)
print(a.value_counts())

count_freq = dict(a['Month'].value_counts())
print(count_freq)



a['count_freq'] = a['Month']
a['count_freq'] = a['count_freq'].map(count_freq)
print(a['Month'][a.count_freq >= a['count_freq'].max()])
print(a['count_freq'].max())
b = a['Month'][a.count_freq >= a['count_freq'].max()]
b = b.unique()
print(b)

c = all_data
c['Month'] = c['Month'].str.upper()
print(c)




#df = a.groupby('Month')
#print(df.count())

'''

#a = take_user_input()
#print(a)

a = find_breed_in_years(user_input)
print("a: ", a)

find_total_registered(user_input)

percentage_top_breeds_over_year(user_input, a)

b = percentage_registered_in_year(user_input, 2021)
#print(f"{b:.6%}")  # 33%

#percentage_top_breeds_over_year(user_input, a)

percentage_top_breeds_all_year(user_input, a)

#total = all_data['Total'][all_data['Year']]
#print(total)

breeds = np.unique(all_data['Breed'])
print(breeds)

months = np.unique(all_data['Month'])
print(months)



for i in breeds:
    for j in months:
        if((percentage_breeds_month(i, j, 2021))):
            print(i, j, percentage_breeds_month(i, j, 2021))

'''

'''

L = []
for i in a:
    for j in months:
        max = np.max(all_data[['Total']][(all_data['Year'] == i) & (all_data['Month'] == j)])
        #the_breed = all_data['Breed'][(all_data['Total'] == max) & (all_data['Year'] == i)]
        #print(i, j, the_breed.values, the_breed == user_input)
        if (not np.isnan(max)):
            print(max, i, j, np.isnan(max))
            the_breed = all_data['Breed'][(all_data['Total'] == max) & (all_data['Year'] == i) & (all_data['Month'] == j)]
            print(the_breed.values)
            L.append(j)
        #if(the_breed.values == user_input):
        #    L.append(j)


print(np.unique(L))

breed_ary = []
month_ary =[]
total_ary = []
for i in breeds:
    for j in months:
        a = np.sum(all_data['Total'][(all_data['Breed'] == i) & (all_data['Month'] == j)])
        print(i, j, np.sum(all_data['Total'][(all_data['Breed'] == i) & (all_data['Month'] == j)]))
        breed_ary.append(i)
        month_ary.append(j)
        total_ary.append(a)
#print(all_data['Total'][(all_data['Year'] == 2021) & all_data['Month'] == 'February'])

print(np.size(breed_ary))
print(np.size(month_ary))

data = np.zeros(np.size(breed_ary), dtype={'names':('Breed', 'Month', 'Total'),
                          'formats':('U30', 'U10', 'i4')})

data['Breed'] = np.array(breed_ary)
data['Month'] = np.array(month_ary)
data['Total'] = np.array(total_ary)

print(data['Breed'][data['Breed'] == user_input])


for i in months:
    b = np.max(data['Total'][data['Month'] == i ])
    c = data[['Breed', 'Total']][data['Total'] == b]
    print(i , b, c)

'''

b = all_data[(all_data['Breed'] == user_input) & (all_data['Year'] == 2022)]

print(b)

c = b[b['Total'] == b['Total'].max()]
print(c)
print(c['Year'].values, c['Month'].values)

a = all_data.groupby('Breed')['Total'].sum()
print(a)

#all_data = pd.read_excel("WeatherData.xlsx", usecols = [2,5,6,7,8,9,10], index_col = [0,1,2,3])
df = pd.read_excel("CalgaryDogBreeds.xlsx", usecols = [0,1,2,3], index_col=[0, 2])
print(df)

dfa = df.groupby('Breed')['Total'].sum()

print(dfa)
print(dfa.loc[user_input])

a = df.loc[2021]
b = a.groupby('Breed')['Total'].sum()
print(b)
print(b.loc[user_input])
print(np.sum(b))

a = df
print(a)
print(a.reset_index())