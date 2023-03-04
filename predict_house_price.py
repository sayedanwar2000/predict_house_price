# -*- coding: utf-8 -*-
"""predict house price.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bwPQyQqQxE59KBNroVRiWzb-YlUf5nIE
"""

import tensorflow as tf

from sklearn.model_selection import train_test_split

from sklearn import metrics

from sklearn.linear_model import LinearRegression

(x_train,y_train),(x_test,y_test)=tf.keras.datasets.boston_housing.load_data(
    path="boston_housing.npz", test_split=0.2, seed=113)

model = LinearRegression()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

MAE= metrics.mean_absolute_error(y_test, y_pred)
MSE=metrics.mean_squared_error(y_test, y_pred)
RMSE= np.sqrt(MSE)

print(MAE)
print(MSE)
print(RMSE)

