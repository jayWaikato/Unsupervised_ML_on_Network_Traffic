import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN


data = np.array([
    [500,  60,   30],[450,  55,   28],[520,  65,   32],   # Normal traffic
    [50,  1500,    2],[45,  1600,    1],  # Possible DDoS traffic
    [600,  70,   35],[510,  75,   33],   # Normal traffic
    [5,  2000,  0.5],[6,  2100,  0.4]   # Possible DDoS traffic
])

dbscan = DBSCAN(eps = 300, min_samples= 2)

model = dbscan.fit(data)

labels = model.labels_

file_name = "DBscan.png"

plt.scatter(data[:, 0], data[:, 1],c = labels,cmap='rainbow')

plt.xlabel("Num of packets")
plt.ylabel("Avg packet size")
plt.title("Network Clustering")
plt.savefig(file_name)
plt.show()
