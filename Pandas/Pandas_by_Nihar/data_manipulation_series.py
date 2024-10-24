import pandas
import numpy

myseries = pandas.Series([1, 13, 41, 5])

## DATA MANIPULATION ##

# doubled = myseries.map(lambda x: x * 2)
# print(doubled)

dupe = myseries.map(lambda x: x *2) ## MAP can be used for series only
print(dupe)

sqrt = myseries.apply(lambda x: x ** 0.5) ## apply can be used for series and dataframes also
print(sqrt)

sorted_s = myseries.sort_values() #  to sort series in ascending order
print(myseries)
print(sorted_s)

drop = myseries.drop(3) # drops the value in index 3 and assigns value to drop variable
print(drop)

drop = myseries.drop(3, inplace=True) ## drops value in index 3 and stores permanently in dataframe and drop variable
print(myseries)
print(drop)

