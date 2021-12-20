import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
dataset = pd.read_csv('student_scores.csv')
shp = dataset.shape
print(shp)
head = dataset.head()
print(head)
taily = dataset.tail()
dscr = dataset.describe()
print(dscr)
dataset.plot(x='Hours', y='Scores', style='o')
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
#plt.show()
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print(regressor.intercept_)
print(regressor.coef_)
#This means that for every one unit of change in hours studied,
#  the change in the score is about 9.91%.
#  Making Predictions
y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)