# DBSCAN Clustering

![DBSCAN Result](DBscan.png)


## 🎯 Overview
DBSCAN (Density-Based Spatial Clustering of Applications with Noise) groups points that are closely packed together, marking as outliers those in low-density regions.  
In this demo, we apply DBSCAN to **network traffic data**—using features such as packet size and inter-arrival time—to discover clusters of similar traffic flows and flag anomalous flows.  
👉 Great for clusters of arbitrary shape and noise detection.


## 📝 Brief Explanation
DBSCAN identifies clusters by looking for areas of high point density. It classifies points as:
- **Core points**: Have at least `min_samples` neighbors within radius `eps`.
- **Border points**: Have fewer than `min_samples` within `eps`, but lie within `eps` of a core point.
- **Noise points**: Neither core nor border—these are the outliers.  
_Tip:_  
- Increase **eps** to join sparser clusters.  
- Increase **min_samples** to make the algorithm more conservative (more noise).


## 🛠️ Files
- `dbscan.py`: Python script demonstrating DBSCAN on a synthetic dataset.  
- `DBscan.png`: Resulting cluster plot.

## 🚀 Run
```bash
python dbscan.py
```
