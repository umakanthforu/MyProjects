import pandas

resource = pandas.read_excel("Data Sets\\student_marks.xlsx")

dataframe = pandas.DataFrame(resource)

# print(dataframe.loc[dataframe["Maths"]>85]) # Simple Condition

# print(dataframe.loc[(dataframe["Maths"]>70) & (dataframe["Maths"]<98)]) ## compound condition

# print(dataframe.loc[(dataframe["English"] > 80) & (dataframe["Maths"] > 80)]) ## compound condition

# print(dataframe.loc[(dataframe["Telugu"] > 30) & (dataframe["Maths"] > 30)]) ## compound condition

# print(dataframe.loc[dataframe["Name"].str.startswith("U")]) ## starts with 

# print(dataframe.loc[dataframe["Name"].str.contains("i")]) ## contains

# print(dataframe.loc[dataframe["Name"].str.endswith("h")]) ## ends with

dataframe["Total"] = dataframe["English"] + dataframe["Hindi"] + dataframe["Telugu"] + dataframe["Maths"] + dataframe["Science"] + dataframe["Social"]


dataframe["Percentage"] = (dataframe["Total"]/600)*100

dataframe["Grade"] = "Pass/Fail"

print(dataframe)

dataframe.loc[dataframe["Percentage"] <= 40,["Grade"]]="Fail"
dataframe.loc[(dataframe["Percentage"] >= 41) & (dataframe["Percentage"] <= 50), ["Grade"]]= "Second Class"
dataframe.loc[dataframe["Percentage"] >= 51, ["Grade"]]= "First Class"


dataframe["Category"]= "To be Decided"

dataframe.loc[dataframe["Percentage"] >= 80, ["Category"]] = "Brilliant"
dataframe.loc[(dataframe["Percentage"] >= 61) & (dataframe["Percentage"] <= 79), ["Category"]] = "Above Average"
dataframe.loc[dataframe["Percentage"] <= 60, ["Category"]]= "Average"



print(dataframe)