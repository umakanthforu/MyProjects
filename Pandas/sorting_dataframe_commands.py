import pandas

df = pandas.DataFrame(pandas.read_excel("Data Sets\\HR_Employee_Data.xlsx"))

# print(df.sort_values("satisfaction_level")) # to print values of column in ascending order

# print(df.sort_values("satisfaction_level", ascending=False)) # to print values of column in descending order

print(df.sort_values(["satisfaction_level", "salary"])) # based on first column given data will be sorted