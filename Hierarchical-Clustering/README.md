# Hierarchical Clustering

![Dendrogram](Hierarchial.png)

## 🎯 Overview
Hierarchical clustering builds nested clusters by merging or splitting them successively.  
In this demo, we apply hierarchical clustering to **network traffic data**—leveraging features like protocol type, byte counts, and flow duration—to uncover traffic patterns at multiple scales.  
👉 Use dendrograms to visualize cluster hierarchy.


## 📝 Brief Explanation
Hierarchical clustering builds a tree of clusters (a dendrogram). There are two main approaches:
- **Agglomerative (bottom-up)**: Start with each point in its own cluster; repeatedly merge the two closest clusters.
- **Divisive (top-down)**: Start with all points in one cluster; repeatedly split clusters.  
_Linkage methods_ (single, complete, average) define how you measure “closest” between clusters.  
To get final clusters, you “cut” the dendrogram at your chosen height.


## 🛠️ Files
- `h_clustering.py`: Python script demonstrating agglomerative clustering on a dataset.  
- `Hierarchial.png`: Sample dendrogram.

## 🚀 Run
```bash
python h_clustering.py
```
