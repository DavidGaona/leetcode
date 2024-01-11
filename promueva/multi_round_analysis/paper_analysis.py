import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kurtosis

# Adjust pandas display options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Loading Data
filepaths = [
    "C:\\Users\\david\OneDrive\\Desktop\\algos\\leetcode\\promueva\\data\\multi_round\\density_10\\200_1_runs_density10.json",
    "C:\\Users\\david\OneDrive\\Desktop\\algos\\leetcode\\promueva\\data\\multi_round\\density_10\\200_2_runs_density10.json",
    "C:\\Users\\david\OneDrive\\Desktop\\algos\\leetcode\\promueva\\data\\multi_round\\density_10\\200_3_runs_density10.json",
    "C:\\Users\\david\OneDrive\\Desktop\\algos\\leetcode\\promueva\\data\\multi_round\\density_10\\200_4_runs_density10.json",
    "C:\\Users\\david\OneDrive\\Desktop\\algos\\leetcode\\promueva\\data\\multi_round\\density_10\\200_5_runs_density10.json",
]
jsons = []

for index, filepath in enumerate(filepaths):
    with open(filepath, 'r') as f:
        data = json.load(f)
        # Adjusting the network names to avoid collisions
        adjusted_data = {"{}_{}".format(network_name, index + 1): value
                         for network_name, value in data.items()}
        jsons.append(adjusted_data)

# Merging all the json data
merged_data = {}
for j in jsons:
    merged_data.update(j)

# Extract FinalReport data and adjust the dataframe structure
final_reports = []
for network_name, network_data in merged_data.items():
    report = network_data['FinalReport']
    report['network_name'] = network_name
    final_reports.append(report)

df = pd.DataFrame(final_reports)

df['total_steps'] = df['totalSteps']
df['agents_data'] = df['AgentCharacteristics']
df = df[['network_name', 'total_steps', 'agents_data']]


# Step 3: Compute the new columns based on the provided requirements

# A function to process each row of the agents_data column
def process_agents_data(row):
    agents = row['agents_data']

    in_favour_speaking = sum(1 for agent in agents if agent['belief'] == 1 and agent['speaking'])
    against_speaking = sum(1 for agent in agents if agent['belief'] == 0 and agent['speaking'])
    in_favour_silent = sum(1 for agent in agents if agent['belief'] == 1 and not agent['speaking'])
    against_silent = sum(1 for agent in agents if agent['belief'] == 0 and not agent['speaking'])

    if in_favour_speaking > against_speaking:
        belief_winner = 1
    elif in_favour_speaking < against_speaking:
        belief_winner = 0
    else:
        belief_winner = 2

    most_popular_agent = max(agents, key=lambda x: x['size'])
    most_popular_won = 1 if most_popular_agent['belief'] == belief_winner else 0
    most_popular_speaking = int(most_popular_agent['speaking'])
    max_size = most_popular_agent['size']
    kurt = kurtosis([agent['size'] for agent in agents])
    total_in_favor = sum(1 for agent in agents if agent['belief'] == 1)
    total_against = len(agents) - total_in_favor

    return pd.Series({
        'belief_winner': belief_winner,
        'in_favour_speaking': in_favour_speaking,
        'against_speaking': against_speaking,
        'in_favour_silent': in_favour_silent,
        'against_silent': against_silent,
        'most_popular_won': most_popular_won,
        'most_popular_speaking': most_popular_speaking,
        'max_size': max_size,
        'kurtosis': kurt,
        'total_in_favor': total_in_favor,
        'total_against': total_against
    })


# Apply the function to each row of the dataframe
df = pd.concat([df, df.apply(process_agents_data, axis=1)], axis=1)

df = df.drop(columns=['agents_data'])

#print(df)

# Descriptive statistics
print(df.describe())

# Distribution of total_steps, max_size, kurtosis
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

sns.histplot(df['total_steps'], ax=axs[0], kde=True)
axs[0].set_title('Distribution of Total Steps')

sns.histplot(df['max_size'], ax=axs[1], kde=True)
axs[1].set_title('Distribution of Max Size')

sns.histplot(df['kurtosis'], ax=axs[2], kde=True)
axs[2].set_title('Distribution of Kurtosis')

plt.tight_layout()
plt.show()

# Exclude the 'network_name' column for correlation
correlation_df = df.drop(columns='network_name')

# Correlation analysis
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Proportion of Majority vs. Minority winning
majority_win_percentage = df[df['belief_winner'] == 1].shape[0] / df.shape[0] * 100
print(f"Percentage of times majority belief wins: {majority_win_percentage:.2f}%")

# Effect of 'most_popular_speaking' on 'belief_winner'
sns.countplot(x='most_popular_speaking', hue='belief_winner', data=df)
plt.title('Effect of Most Popular Node Speaking on Winning Belief')
plt.show()

# Kurtosis vs. Winner
sns.boxplot(x='belief_winner', y='kurtosis', data=df)
plt.title('Kurtosis vs Winning Belief')
plt.show()

