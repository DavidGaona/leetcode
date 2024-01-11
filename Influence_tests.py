agents = dict()

# Agent BASE
agents["Agent A"] = {"b": 0.75, "ct": 0.4, "c": 0.8}
neighbor_list = ["Agent B", "Agent C", "Agent D"]

# Neighbor 1
agents["Agent B"] = {"b": 0.8, "ct": 0.4, "c": 1.0}

# Neighbor 2
agents["Agent C"] = {"b": 0.2, "ct": 0.3, "c": 1.0}

# Neighbor 3
agents["Agent D"] = {"b": 0.2, "ct": 0.3, "c": 1.0}

new_confidence = 0
total_confidence = 0
individual_influence = []
for agent in agents:
    if agent not in neighbor_list:
        continue
    round_influence = agents[agent]["b"] * agents[agent]["c"]
    total_confidence += round_influence
    individual_influence.append(round_influence)

num = 0
for agent in agents:
    if agent not in neighbor_list:
        continue
    print(agent, "influence is:", round(individual_influence[num] / total_confidence, 4))
    num += 1

import math

math.exp(-2)
math.log(2, math.e)

