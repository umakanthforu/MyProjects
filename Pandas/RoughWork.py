import pandas

df = pandas.read_excel("Data Sets\\student_marks.xlsx")


dataframe = pandas.DataFrame(df)
# print(dataframe)

# print(dataframe)

df["Total"]= df["English"]+df["Hindi"]

print(dataframe)