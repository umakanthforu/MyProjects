import boto3
import pandas

rawdata = pandas.read_excel("student_marks.xlsx")

dataframe = pandas.DataFrame(rawdata)

print(dataframe.size)