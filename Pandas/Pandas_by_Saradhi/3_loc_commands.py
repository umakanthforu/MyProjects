import pandas

df = pandas.DataFrame(pandas.read_excel("Data Sets\\HR_Employee_Data.xlsx"))

### loc commands are denoted using column name ###

# print(df.loc[234]) # to access with row number

# print(df.loc[234,["Emp_Id"]]) # to access with row number and specific column

# print(df.loc[0:10]) # to show data in rows mentioned start and stop numbers are included.

# print(df.loc[0:10, "Emp_Id"]) # to show data in rows mentioned with specific columns

# print(df.loc[0:10,["Emp_Id", "Department"]]) # to show data in rows and specific columns

# print(df.loc[0:10, "Emp_Id" : "Department"]) # to show data in rows and between columns

