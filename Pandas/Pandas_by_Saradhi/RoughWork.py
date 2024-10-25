import pandas

resource = pandas.read_excel("Data Sets\\student_marks.xlsx", sheet_name = "markssheet_missing")

dataframe = pandas.DataFrame(resource)

# dataframe["Total"]=dataframe["English"]+dataframe["Hindi"]+dataframe["Telugu"]+dataframe["Maths"]+dataframe["Science"]+dataframe["Social"]

# dataframe["Percentage"] = (dataframe["Total"]/600)* 100

# dataframe["Grade"]= "Under Progress"

# # print(dataframe.loc[(dataframe["English"] > 80) & (dataframe["Maths"] > 60)])

# dataframe.loc[dataframe["Percentage"] >= 70, ["Grade"]]= "Excellent"
# dataframe.loc[(dataframe["Percentage"] >= 60) & (dataframe["Percentage"] <= 69), ["Grade"]]= "Above Average"
# dataframe.loc[(dataframe["Percentage"] >= 50) & (dataframe["Percentage"] <= 59), ["Grade"]]= "Average"
# dataframe.loc[dataframe["Percentage"] <= 49, ["Grade"]]= "Below Average"
# print(dataframe.sort_values("Percentage", ascending=False))

print(dataframe.fillna("Replaced"))

print(dataframe.dropna())
