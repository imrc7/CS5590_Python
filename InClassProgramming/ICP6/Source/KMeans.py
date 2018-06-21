import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from numpy import genfromtxt


X = pd.read_csv("D:\\Summer 18\\Lesson6\\Python_Lesson6\\sample_stocks.csv")
X= np.array(X)


# no. of clusters
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Coordinates of cluster centers
centroids = kmeans.cluster_centers_
# Labels of each point
labels = kmeans.labels_

colors = ["g.","r.","c.","y."]

for i in range(len(X)):
    #print("coordinate:",X[i], "label:", labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)


plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)

plt.show()

-------------- Bonus elbow method (http://www.scikit-yb.org/en/latest/api/cluster/elbow.html)
# Elbow Method - Technique to determine the best value for K
# Plot a line graph of the SSE for each value of k.
# If the line graph looks like an arm - a red circle in below line graph (like angle),
# the "elbow" on the arm is the value of optimal k (number of cluster).
# Here, we want to minimize SSE. SSE tends to decrease toward 0 as we increase k
# because then each data point is its own cluster, and there is no error between it and the center of its cluster).
# So the goal is to choose a small value of k that still has a low SSE, and the elbow usually represents where we start to have diminishing returns by increasing k.



temp = {}
# Selecting k in range of 1 to 5
for k in range(1,5):
    kmeans = KMeans(n_clusters=k).fit(X)

# to find distances we use inertia
    temp[k] = kmeans.inertia_

plt.plot(list(temp.keys()), list(temp.values()))
plt.show()








