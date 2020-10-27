# Linear Regression Single Variable

# First we import the dataframe (CSV of houseprices)
# Next we plot a scatter plot to get an idea of the distribution



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# First we load in the data
df = pd.read_csv('homeprices.csv')

# Here we set up a graph to show the data points before any predictions
plt.xlabel('area (sqr ft)')
plt.ylabel('price (US$)')
plt.scatter(df.area, df.price, color='red', marker='+')
plt.show()

# Here we train the model using sklearn by passing in the csv file
reg = linear_model.LinearRegression()
reg.fit(df[['area']], df.price)

# Set the variable for the price we want to predict
x = 3300

# Here we predict the price
prediction = reg.predict([[x]])
print('The predicted price for a 3300 sqft home is: {}'.format(prediction))

# To prove this is correct we can find the coefficient and and intercept of our line (where mx+b=y where m is the coefficient and b is the intercept)

# coefficient (m)
m = reg.coef_
print('The coefficient is: {}'.format(int(m)))

# Intercept (b)
b = reg.intercept_
print('The intercept is: {}'.format(int(b)))


# Now see the output of the equasion to see if it is the same as the output from our linear regression algorithm

print('mx+b = {}'.format(m*x+b))
print('Linear Regression prediction: {}'.format(prediction))

# Plot the final results
plt.xlabel('area', fontsize=20)
plt.ylabel('price', fontsize=20)
plt.scatter(df.area, df.price, color='red', marker='+')
plt.plot(df.area, reg.predict(df[['area']]), color='blue')
plt.show()








