import pandas as pd
import numpy as np

myseries = pd.Series([23, 34, 45, None, 1])

print(myseries.isnull()) # prints boolean value of missing values

print(myseries.notnull()) # prints boolean value of not null values

print(myseries.fillna("Apple")) # it fills the null value with Apple