import json
import matplotlib.pyplot as plt

# Load the JSON data
with open('C:\\Users\\david\\OneDrive\\Desktop\\algos\\leetcode\\promueva\\data\\single_data2.json', 'r') as f:
    data = json.load(f)

# Extract the round reports
round_reports = data['Network1']['RoundReport']

# Extract rounds and the four categories of interest
rounds = [report['Round'] for report in round_reports]
inFavourSpeaking = [report['inFavourSpeaking'] for report in round_reports]
againstSpeaking = [report['againstSpeaking'] for report in round_reports]
inFavourSilent = [report['inFavourSilent'] for report in round_reports]
againstSilent = [report['againstSilent'] for report in round_reports]

# Plot stacked area chart
plt.figure(figsize=(12, 6))

plt.stackplot(rounds,
              inFavourSilent, inFavourSpeaking, againstSpeaking, againstSilent,
              labels=['In Favor (Silent)', 'In Favor (Speaking)', 'Against (Speaking)', 'Against (Silent)'],
              alpha=0.6)

plt.title("Evolution of Agent Opinions over Rounds")
plt.xlabel("Round")
plt.ylabel("Number of Agents")
plt.legend(loc='upper right')  # Adjusted location to 'upper right'
plt.margins(0, 0)  # Set margins to avoid "whitespace"
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()
