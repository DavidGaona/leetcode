import json
import numpy as np
import pandas as pd

# Adjust pandas display options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Load the JSON data
with open('C:\\Users\\david\\OneDrive\\Desktop\\algos\\leetcode\\promueva\\data\\single_data2.json', 'r') as f:
    data = json.load(f)

# Extract Agent Characteristics for Initial Report
agent_data = data['Network1']['InitialReport']['AgentCharacteristics']

# Convert it to DataFrame for easier analysis
df = pd.DataFrame(agent_data)

# Descriptive Statistics
stats = pd.DataFrame()

# Calculating statistics for each relevant column
for column in ['size', 'belief', 'willingness', 'confidence', 'climate']:
    stats.at[column, 'Mean'] = df[column].mean()
    stats.at[column, 'Median'] = df[column].median()
    stats.at[column, 'Std Dev'] = df[column].std()
    stats.at[column, 'Min'] = df[column].min()
    stats.at[column, 'Max'] = df[column].max()
    stats.at[column, '1%'] = df[column].quantile(0.01)
    stats.at[column, '25%'] = df[column].quantile(0.25)
    stats.at[column, '75%'] = df[column].quantile(0.75)
    stats.at[column, '99%'] = df[column].quantile(0.99)
    stats.at[column, 'IQR'] = stats.at[column, '75%'] - stats.at[column, '25%']
    stats.at[column, 'Skewness'] = df[column].skew()
    stats.at[column, 'Kurtosis'] = df[column].kurt()

print(stats)
