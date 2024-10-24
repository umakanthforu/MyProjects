import pandas

resource = pandas.read_excel("Data Sets\\student_marks.xlsx", sheet_name = "markssheet_missing")

dataframe = pandas.DataFrame(resource)

# print(dataframe.fillna(65)) ## fills given value in missing place but not written to dataframe

# print(dataframe.dropna()) ## removes rows with missing values temporarily and not in dataframe

dataframe.dropna(inplace=True) ## removes rows with missing values permanently from dataframe

print(dataframe.info())