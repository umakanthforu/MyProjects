import pandas

## for creating a dataframe by reading a excel file
dataframe = pandas.read_excel("Data Sets\\HR_Employee_Data.xlsx")

# print(dataframe.head()) ## it shows top 5 records by default

# print(dataframe.head(3)) ## it shows top 3 records as mentioned in Argument

# print(dataframe.tail()) ## it prints last 5 records by default

# print(dataframe.tail(2)) ## it prints last 2 records as mentioned in Argument 

# print(dataframe.describe()) ## it gives count, mean, min, max of all columns 

# print(dataframe.shape) # to show the number of rows and column

print(dataframe.info()) # to show the columns and dattypes and size of dataframe

# print(dataframe[0:21:1]) # to print rows from index 0 to 20 with 1 difference (start, stop and step arguments)

# print(dataframe[1:21:2]) # to print rows from index 0 to 20 with 2 difference (start, stop and step arguments)

# print(dataframe["satisfaction_level"]) # to display rows of the specified column name

# print(dataframe[["Emp_Id","Department", "salary"]]) # to display rows of mutiple columns speicified by names

# print(dataframe[["Emp_Id", "Department", "salary"]][0:10:1]) # to display rows of multple columns based on start, stop and step arguments

# for item in dataframe.iterrows(): # to print in tuple format of each value
    # print(item)