import numpy as np
#fst = np.arange(1,9)
#print(fst)
import altair as alt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import datasets
import matplotlib.pyplot as plt
iris = datasets.load_iris()
#print(iris.keys)
#print(iris.data)
#print(iris.target)
#print(iris.DESCR)
x = iris.data
y = iris.target
print('Iris data shape is:', x.shape)
print('Iris data shape is:', y.shape)
print('Iris different groups:', len(np.unique(y)))
def plot_clusters(x, idx1, idx2, y = None,):
    """
            idx1: represents the x axis feature
            idx2: represents the y axis feature
            y: represents the values to assign colour with
    """
    plt.scatter(x[:,idx1],x[:,idx2], c=y)
    plt.show()
k = 3
idx1 = 0
idx2 = 1
plot_clusters(x, idx1, idx2)
plot_clusters(x, idx1, idx2, y)
kMeans = KMeans(n_clusters=k, random_state=42)
y_pred = kMeans.fit_predict(x)
plot_clusters(x, idx1, idx2, y_pred)