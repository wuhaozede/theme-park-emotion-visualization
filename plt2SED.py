import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# Load the CSV file
file_path = r'data.csv'
data = pd.read_csv(file_path, encoding='utf-8', header=[0, 1])

# Convert the data to numeric, ignoring non-numeric columns
data = data.apply(pd.to_numeric, errors='ignore')

# Define the groups
groups = ['TM', 'TF', 'AM', 'AF', 'OM', 'OF']

# Function to calculate and plot the confidence ellipse
def plot_confidence_ellipse(x, y, ax, n_std=2.0, facecolor='none', **kwargs):
    if x.size != y.size:
        raise ValueError("x and y must be the same size")
    
    cov = np.cov(x, y)
    pearson = cov[0, 1] / np.sqrt(cov[0, 0] * cov[1, 1])
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2, facecolor=facecolor, **kwargs)
    
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)
    
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)
    
    transf = (plt.gca().transData
              .rotate_deg(45)
              .scale(scale_x, scale_y)
              .translate(mean_x, mean_y))
    
    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)

# Plot each group
for group in groups:
    vis_col = (group, 'VIS')
    ais_col = (group, 'AIS')
    
    vis_data = data[vis_col]
    ais_data = data[ais_col]
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(vis_data, ais_data, alpha=0.5, label=f'{group} Data Points')
    
    plot_confidence_ellipse(vis_data.values, ais_data.values, ax, edgecolor='red')
    
    ax.set_xlabel('VIS')
    ax.set_ylabel('AIS')
    ax.set_title(f'{group} VIS vs AIS with Confidence Ellipse')
    ax.legend()
    ax.grid(True)
    plt.savefig(f'{group}_confidence_ellipse.png')  # Save the figure
    plt.show()

