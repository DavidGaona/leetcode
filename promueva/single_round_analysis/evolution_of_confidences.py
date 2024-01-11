import json
import matplotlib.pyplot as plt

# Load the JSON data
with open('C:\\Users\\david\\OneDrive\\Desktop\\algos\\leetcode\\promueva\\data\\single_data.json', 'r') as f:
    data = json.load(f)

# Extract the round reports
round_reports = data['Network1']['RoundReport']

# Extract rounds, confidences for speaking, and confidences for silence
rounds = [report['Round'] for report in round_reports]
confidence_diff_speaking = [report['totalConfidenceInFavourSpeaking'] - report['totalConfidenceAgainstSpeaking'] for report in round_reports]
confidence_diff_silence = [report['totalConfidenceInFavourSilent'] - report['totalConfidenceAgainstSilent'] for report in round_reports]

# Plot the data
plt.figure(figsize=(10,6))

plt.plot(rounds, confidence_diff_speaking, label="Confidence Difference (Speaking)", marker='o')
plt.plot(rounds, confidence_diff_silence, label="Confidence Difference (Silence)", marker='x')

plt.title("Evolution of Beliefs over Rounds")
plt.xlabel("Round")
plt.ylabel("Difference in Confidence")
plt.legend()
plt.grid(axis='y', linestyle='--')
plt.tight_layout()

plt.show()
