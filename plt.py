import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r'data.csv'
data = pd.read_csv(file_path, encoding='utf-8', header=[0, 1])

# Convert the data to numeric, ignoring non-numeric columns
data = data.apply(pd.to_numeric, errors='ignore')

# Define the groups
groups = ['TM', 'TF', 'AM', 'AF', 'OM', 'OF']

# Plot each group
for group in groups:
    vis_col = (group, 'VIS')
    ais_col = (group, 'AIS')
    
    plt.figure(figsize=(8, 6))
    plt.scatter(data[vis_col], data[ais_col], alpha=0.5, label=f'{group} Data Points')
    plt.xlabel('VIS')
    plt.ylabel('AIS')
    plt.title(f'{group} VIS vs AIS')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{group}_scatter_plot.png')  # Save the figure
    plt.show()
