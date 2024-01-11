import json
import matplotlib.pyplot as plt

# Load the JSON data
with open('C:\\Users\\david\\OneDrive\\Desktop\\algos\\leetcode\\promueva\\data\\single_data.json', 'r') as f:
    data = json.load(f)

# Extract the 'size' attribute from each AgentCharacteristicsItem in the initial report
sizes = [item['size'] for item in data['Network1']['InitialReport']['AgentCharacteristics']]

# Plot a histogram
plt.hist(sizes, bins=20, edgecolor="k", alpha=0.7)
plt.title("Histogram of Agent Sizes")
plt.xlabel("Size")
plt.ylabel("Number of Agents")
plt.grid(axis='y', linestyle='--')
plt.tight_layout()

plt.show()


