import pandas as pd
import numpy as np

myseries = pd.Series([1, 3, 4, 7])

print(myseries.describe())

print(myseries.max()) # Max
print(myseries.min()) # Min
print(myseries.std()) # Standard Deviation
print(myseries.mean()) # Mean