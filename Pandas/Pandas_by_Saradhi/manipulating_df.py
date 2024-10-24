import pandas

data = pandas.read_excel("Data Sets\\student_marks.xlsx")

df = pandas.DataFrame(data)

# Adding Columns

# df["Total Marks"] = 0  # to create a column with name Total Marks and value as 0

# # create a column with formula to add all the values of mentioned columns
# df["Total Marks"] = df ["English"] + df["Hindi"] + df["Telugu"] + df["Maths"] + df["Science"] + df["EVS"] + df["Sports"] + df["AI"] + df["Sanskrit"]

## Dropping Columns

print(df.drop(columns="AI"))  # Drops the column just for display purpose

df.drop(columns="AI", inplace=True) # Drops the column from Dataframe permanently
print(df)