import pandas as pd

# Load the CSV file
file_path = r'data.csv'
data = pd.read_csv(file_path, encoding='utf-8', header=[0, 1])

# Convert the data to numeric, ignoring non-numeric columns
data = data.apply(pd.to_numeric, errors='ignore')

# Define the groups
groups = ['TM', 'TF', 'AM', 'AF', 'OM', 'OF']

# Initialize a dictionary to store the results
results = {}

# Calculate statistics for each group
for group in groups:
    vis_col = (group, 'VIS')
    ais_col = (group, 'AIS')
    
    group_stats = {
        'VIS_mean': data[vis_col].mean(),
        'VIS_std': data[vis_col].std(),
        'VIS_min': data[vis_col].min(),
        'VIS_max': data[vis_col].max(),
        'AIS_mean': data[ais_col].mean(),
        'AIS_std': data[ais_col].std(),
        'AIS_min': data[ais_col].min(),
        'AIS_max': data[ais_col].max()
    }
    
    results[group] = group_stats

# Convert the results to a DataFrame
results_df = pd.DataFrame(results)

# Display the results
print(results_df)
