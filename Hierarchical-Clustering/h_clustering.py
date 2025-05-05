import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage,dendrogram

data = np.array([
    [500,  60,   30],[450,  55,   28],[520,  65,   32],   # Normal traffic
    [50,  1500,    2],[45,  1600,    1],  # Possible DDoS traffic
    [600,  70,   35],[610,  75,   33],   # Normal traffic
    [5,  2000,  0.5],[6,  2100,  0.4]   # Possible DDoS traffic
])

linked = linkage(data,method='ward')

file_name = "Hierarchial.png"

plt.figure(figsize=(10,7))

dendrogram(linked,orientation='top',labels=(np.arange(1,10)),distance_sort='descending',show_leaf_counts=True)

plt.title("hierarchial clustering dendogram")

plt.xlabel('Data Points')

plt.ylabel('Distance')
plt.savefig(file_name)
plt.show ()
