import pandas as pd
import matplotlib.pyplot as plt

#Reading Data
titanic_data_set = pd.read_csv(r'C:\Users\lkouteich\Downloads\titanic\tested.csv')
num_of_rows, num_of_cols = titanic_data_set.shape
print('There are {} rows and {} columns in testing sheet'.format(num_of_rows,num_of_cols))

print('\n')
print('\n')

#making data proper by checking which of the column has null values
need_to_clean_columns = []
for i in titanic_data_set.columns:
    print(i +' has : '+str(titanic_data_set[i].isnull().sum())+' null data')
    if titanic_data_set[i].isnull().sum() > 0:
        need_to_clean_columns.append(i)


#printing which column needs to be cleaned
print(need_to_clean_columns)

#cleaning the data
for i in need_to_clean_columns:
    if i == 'Age':
        titanic_data_set[i] = titanic_data_set[i].fillna(titanic_data_set[i].mean())
    elif i == 'Fare':
        titanic_data_set[i] = titanic_data_set[i].fillna(0)
    elif i == 'Cabin':
        titanic_data_set[i] = titanic_data_set[i].fillna('UnKnown')

