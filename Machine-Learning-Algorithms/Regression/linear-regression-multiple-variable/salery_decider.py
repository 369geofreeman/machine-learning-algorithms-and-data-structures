# A script that uses multivariable linear regression to predict the correct
# salary for a new employee based on his experience, test score (out of 10) 
# and interview score (out of 10)


import numpy as np
import pandas as pd
import math


df = pd.reaad_csv('hiring.csv')

median_test_scores = math.floor(df.test_score(out-of10).median() )

print(median_test_scores)



