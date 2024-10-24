import pandas

## creating a dictionary 
mydict = {
    "Name" : ["Rana", "Rama", "Umakanth", "Priyanka", "Karthika"],
    "Percentage" : [76, 56, 89, 98, 99]
}

# data = pandas.read_("Data Sets\\HR_Employee_Data.xlsx") # to read the file and copy to variable data

dataframe = pandas.DataFrame(mydict) # to create dataframe from the read data

print(dataframe)