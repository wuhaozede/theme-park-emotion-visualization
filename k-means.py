import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the CSV file
file_path = r'E:\姜老师小组\SIC\3月30日统计表.csv'
data = pd.read_csv(file_path, encoding='utf-8', header=[0, 1])

# Convert the data to numeric, ignoring non-numeric columns
data = data.apply(pd.to_numeric, errors='ignore')

# Define the groups
groups = ['TM', 'TF', 'AM', 'AF', 'OM', 'OF']

# Function to perform t-mean clustering
def t_mean_clustering(x, y, n_clusters=3, n_resamples=10):
    best_inertia = np.inf
    best_centers = None
    for _ in range(n_resamples):
        kmeans = KMeans(n_clusters=n_clusters, n_init=1)
        kmeans.fit(np.column_stack((x, y)))
        if kmeans.inertia_ < best_inertia:
            best_inertia = kmeans.inertia_
            best_centers = kmeans.cluster_centers_
    return best_centers

# Plot each group with t-mean clustering
for group in groups:
    vis_col = (group, 'VIS')
    ais_col = (group, 'AIS')
    
    vis_data = data[vis_col]
    ais_data = data[ais_col]
    
    cluster_centers = t_mean_clustering(vis_data.values, ais_data.values) # The actual parameters need to be adjusted
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(vis_data, ais_data, alpha=0.5, label=f'{group} Data Points')
    ax.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', marker='x', label='Cluster Centers')
    
    ax.set_xlabel('VIS')
    ax.set_ylabel('AIS')
    ax.set_title(f'{group} VIS vs AIS with T-Mean Clustering')
    ax.legend()
    ax.grid(True)
    plt.savefig(f'{group}_t_mean_clustering.png')  # Save the figure
    plt.show()
