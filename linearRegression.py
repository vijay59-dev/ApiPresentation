# Import the packages and classes needed in this example:
import numpy as np
from sklearn.linear_model import LinearRegression

# Create a numpy array of data:
x = np.array([10,20,25,28]).reshape((-1, 1))
print(x)
y = np.array([21,25,29,32])

# Create an instance of a linear regression model and fit it to the data with the fit() function:
model = LinearRegression().fit(x, y)

# Predict a Response and print it:
y_pred = model.predict(np.array([37]).reshape(-1,1))
print('Predicted response:', y_pred, sep='\n')