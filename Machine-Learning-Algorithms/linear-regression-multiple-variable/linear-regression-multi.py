# Linear regression with multiple variables to predict the price of a house


import pandas as pd
import numpy as np
from sklearn import linear_model
import math


# Load in the data using pandas
df = pd.read_csv("homeprices.csv")


# We have a gap in our dataset where one of the 'num of bedrooms' is empty
# To get around this we will get the median of all the 'num of bedrooms'
# and use that as a safe assumption to what it might have been

median_bedrooms = math.floor(df.bedrooms.median())

# And now to fill the empty cells with our new data

df.bedrooms = df.bedrooms.fillna(median_bedrooms)


# Now the data is cleaned up we will create our linear regression class object

reg = linear_model.LinearRegression()

# train our model

reg.fit(df[['area', 'bedrooms', 'age']], df.price)

# Here we can see our coefficients
print('the coefficients are:', reg.coef_)


# And here we can see our intercept
print('The intercept is:', reg.intercept_)


# Now we can predict the price based on 3000sqft, 3 bedrooms and 40 years old 

prediction = reg.predict([[3000, 3, 40]])

# And print the results

print("The price of a house of 3000sqft with 3 bedrooms and is 40 years old is ${}".format(round(float(prediction), 2)))


# Finally to see how it came up with that price, and to check the math. We can do do the sum we found in the method, which is the coefficients multiplied by the features plus the intercept. So:

math_check = ((112.06*3000)+(23388.88*3)+(-3231.72*40)+221323.00)

print('prediction is {}. And our calculation is {}'.format(prediction, math_check))

# Which shows us that linear regression with multiple variables is correct.
