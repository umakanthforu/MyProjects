import pandas

# response = pandas.read_excel("Data Sets\\student_marks.xlsx")

## sheet_name is to mention sheet of excel file ##
response = pandas.read_excel("Data Sets\\student_marks.xlsx", sheet_name = "markssheet_dup")
dataframe = pandas.DataFrame(response)

## knowing duplicate is there or not ##

# print(dataframe.duplicated()) # it gives boolen output with duplicate if false then not available

## REMOVING DUPLICATES ##

print(dataframe.drop_duplicates()) ## just displays without duplicates, but dataframe has duplicate entries

print(dataframe.drop_duplicates(inplace=True)) ## removes the duplicate entries from dataframe

print(dataframe.duplicated())