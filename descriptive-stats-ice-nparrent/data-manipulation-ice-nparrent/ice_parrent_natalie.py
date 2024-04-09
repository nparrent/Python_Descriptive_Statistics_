###############################
#       Read in Libraries     #
###############################
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold

################################
#     Set Working Directory    #
################################
os.getcwd()
os.chdir(r'\Users\npleg\OneDrive\Documents\GitHub\Python\data-manipulation-ice-nparrent\data')


################################
#         Read in Data         #
################################
car_data = pd.read_table('car.test.frame.txt', sep='\t')
#print(car_data)



################################
#         Accessing Data       #
################################

#What the column header names are
car_data.columns

# Determine the number of columns
len(car_data.columns)

# Determine the number of rows
len(car_data.index)

# Determine which columns are categorical and convert them from object to category
car_data['Country'] = car_data['Country'].astype('category')

car_data['Type'] = car_data['Type'].astype('category')

# How many unique values does Type have?
print("\nUnique Type Values")
pd.unique(car_data.Type)

# How many unique values does Country have?
print("\nUnique Country Values")
pd.unique(car_data.Country)

# What is the value of the 57th row and 3rd column?
print("\n 57th Row, 3rd Column")
car_data.iloc[56,2]

# What are the values for the 24th row?
print("\n24th Row:")
car_data.iloc[24]


# Using three different methods, select row with index value 29 with 1st, 2nd, 3rd columns
print("\nMethod 1")
car_data.iloc[29,0:3]

print("\nMethod 2")
car_data.iloc[[29],[0,1,2]]

print("\nMethod 3")
car_data.loc[29,'Price':'Reliability']

# Using two different ways, select the row with index value 45 with the 3rd and 7th columns
print("\nMethod 1")
car_data.iloc[[45],[2,6]]

print("\nMethod 2")
car_data.loc[45,['Reliability', 'Disp.']]
car_data.columns

# Create a new dataframe for the column HP using two different methods
car_data1 = car_data.loc[:, ['HP']]
car_data1

car_data2 = car_data.iloc[:, [7]]
car_data2


################################
#  Sorting and Ordering Data   #
################################

# Select compact cars that have a reliability greater than and equal to 4.
print("\nCompact Cars with Reliability Greater = to 4")
car_data[(car_data.Type == 'Compact')&(car_data.Reliability >= 4.0)]

# Find compact cars that have a reliability greater than and equal to 3 from Japan, but not from the US
print("\nReliability Greater = to 3 and From Japan not US")
car_data[(car_data.Reliability >= 3)&(car_data.Type == 'Compact')&((car_data.Country=='Japan')&(car_data.Country!='USA'))]

# How many cars are manufactured with the label Japan/USA?
len(car_data[car_data.Country=='Japan/USA'])

# How many cars are manufactured in the US or Japan?
len(car_data[(car_data.Country=='Japan')|(car_data.Country!='USA')|(car_data.Country!='Japan/USA')])

# How many cars are manufactured in the US or Japan with a reliability greater than and equal to 4?
len(car_data[(car_data.Reliability >= 4)&((car_data.Country=='Japan')|(car_data.Country!='USA')|(car_data.Country!='Japan/USA'))])

# Create a subsample of 70% of your data
car_data_sample = car_data.sample(frac=0.7, replace=False)
len(car_data_sample.index)

# Create samples for a 8-fold cross validation test
pd.notnull(car_data)

kf = KFold(n_splits=8)

for train, test in kf.split(car_data):
    print("%s %s" % (train, test))

car_data.iloc[train]

car_data.iloc[test]

# Select columns that are numeric and save it as a new dataframe
new_data = car_data.select_dtypes(include = ["int64"])
new_data.head()
new_data.info()

# Remove the columns HP and Price from the dataframe
new_data.drop(['HP', 'Price'], axis=1)

# Save the columns Country and Weight as a new datafame
two_data = car_data[['Country', 'Weight']]
two_data.columns

# Rename these two columns in the new dataframe
two_data.rename(columns={'Country':'Orgin Country'}, inplace=True)
two_data.rename(columns={'Weight':'Total Weight'}, inplace=True)
two_data.columns

#two_data.columns = ['Orgin Country', 'Total_Weight']

