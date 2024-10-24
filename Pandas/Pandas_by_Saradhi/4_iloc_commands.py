import pandas

df = pandas.read_excel("Data Sets\\HR_Employee_Data.xlsx")

dataset = pandas.DataFrame(df)

### iloc commands are denoted using column number ###

# print(dataset.iloc[0:10]) # excludes 10 th row and prints till 9

# print(dataset.iloc[0,10]) # excludes 0 th row of 10th column

# print(dataset.iloc[0:10,1]) # prints 0 th row and 1st column data

# print(dataset.iloc[0:5,0:3]) # to print data for 5 rows of 3 columns

# print(dataset.iloc[[1,3,5,6]]) # to print specific indexed rows

# print(dataset.iloc[[1,3,4,6],[6,9]])  # to print specific rows of specific columns

# print(dataset.iloc[:,[0, 5, 7]]) # to print all rows of indexed columns

# print(dataset.iloc[0:20:2, [2, 4 ,6]]) # to print 0 to 20 rows with skip value and selected rows

# print(dataset.iloc[0:20:2, 2:7 ]) # to print 0 to 20 rows with skip value for range of columns
