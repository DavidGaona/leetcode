from random import randrange, uniform, choice, seed
import numpy as np
import matplotlib.pyplot as plt

seed(10)


def uniform_round(num1, num2, digits=4):
    return round(uniform(num1, num2), digits)


def custom_print(arr):
    for result in arr:
        print(result)


def euclidean_distance(x1, y1, x2, y2):
    p1 = np.array((x1, y1))
    p2 = np.array((x2, y2))
    distance = np.linalg.norm(p2 - p1)
    return round(distance, 4)


# x1, y1, x2, y2
corners = [0.0, 0.0, 1000.0, 1000.0]

# x1, x2, y1, y2
rivers = [
    [0.0, 200.0, 278.5, 358.73],
    [200.0, 220.0, 258.5, 368.73],
    [220.0, 600.0, 248.5, 378.73],
    [600.0, 1000.0, 265.22, 368.3]
]

rocks = []

num_of_rocks = 2000
max_x_size = 20
max_y_size = 20
for i in range(num_of_rocks):
    x_cord = uniform_round(0, corners[2] - 10)
    x_add = uniform_round(1, max_x_size)

    y_cord = uniform_round(0, corners[3] - 10)
    y_add = uniform_round(1, max_y_size)
    rocks.append([x_cord, round(x_cord + x_add, 4), y_cord, round(y_cord + y_add, 4)])

building_dims = (200, 200)

possible_placements = []
number_of_runs = []


def reset():
    global possible_placements, number_of_runs
    possible_placements = []
    number_of_runs = []


# Custom rocks and river
"""
rivers = []
# x1, x2, y1, y2
rocks = [
    [250, 750, 0, 1000],
    [0, 1000, 250, 750]
]
"""
obstacles = rivers + rocks


def is_between(c1, c2, c3, c4):
    if c1 < c3 < c2:
        return True
    elif c1 < c4 < c2:
        return True
    elif c3 < c1 < c4:
        return True
    elif c3 < c2 < c4:
        return True
    return False


def move(center, min_step_size=0, max_step_size=20, fixed_step_size=False, fixed_step_size_x=20, fixed_step_size_y=20):
    move_by_x = uniform_round(min_step_size, max_step_size)
    move_by_y = uniform_round(min_step_size, max_step_size)
    if fixed_step_size:
        move_by_x = fixed_step_size_x
        move_by_y = fixed_step_size_y
    new_x = round(center[0] + (move_by_x * choice([1, -1])), 4)
    new_y = round(center[1] + (move_by_y * choice([1, -1])), 4)
    return new_x if 0.0 + building_dims[0] // 2 <= new_x <= corners[2] - building_dims[0] // 2 else center[0], \
           new_y if 0.0 + building_dims[1] // 2 <= new_y <= corners[2] - building_dims[1] // 2 else center[1]


def verify_collisions(center, half_length_x, half_length_y):
    counter = 0
    score = 0
    for obstacle in obstacles:
        collides_x = is_between(center[0] + half_length_x, center[0] - half_length_x, obstacle[0], obstacle[1])
        collides_y = is_between(center[1] + half_length_y, center[1] - half_length_y, obstacle[2], obstacle[3])
        score += euclidean_distance(center[0], center[1], (obstacle[0] + obstacle[1]) / 2,
                                    (obstacle[2] + obstacle[3]) / 2)
        if collides_x and collides_y:
            counter += 1

    return counter, score


def single_run(min_prob, fixed=False, fixed_x=20, fixed_y=20, min_range=0, max_range=20):
    center = [uniform_round(0 + building_dims[0], 1000 - building_dims[0]),
              uniform_round(0 + building_dims[1], 1000 - building_dims[1])]
    half_length_x = building_dims[0] / 2
    half_length_y = building_dims[1] / 2
    num_collisions, score = verify_collisions(center, half_length_x, half_length_y)
    num_changes = 0
    while num_collisions != 0:
        past_center = center.copy()
        past_collisions = num_collisions
        past_score = score
        center[0], center[1] = move(center, min_range, max_range, fixed, fixed_x, fixed_y)
        num_collisions, score = verify_collisions(center, half_length_x, half_length_y)
        if score < past_score:
            prob_to_move = uniform(0.0, min_prob)
        else:
            prob_to_move = uniform(0.75, 1.0)
        roll = uniform(0, 1)
        if prob_to_move < roll:
            center = past_center
        num_changes += 1
    center.append(num_changes)
    number_of_runs.append(num_changes)
    possible_placements.append(center)


def simulate(num_runs, min_prob, id_sim, fixed=False, fixed_x=20, fixed_y=20, min_range=0, max_range=20):
    global data_of_runs
    while len(possible_placements) < num_runs:
        single_run(min_prob, fixed, fixed_x, fixed_y, min_range, max_range)
    cum_sum = 0
    max_runs = possible_placements[0][2]
    min_runs = possible_placements[0][2]
    for valid_placement in possible_placements:
        cum_sum += valid_placement[2]
        max_runs = max(valid_placement[2], max_runs)
        min_runs = min(valid_placement[2], min_runs)
    mean_runs = round(cum_sum / len(possible_placements), 4)
    # custom_print(possible_placements)
    possible_placements.sort(key=lambda x: x[2])
    median_run = np.median(np.array(number_of_runs))
    # print(f"\nAverage runs: {mean_runs}\nMedian run: {median_run}\n"
    #      f"Max runs: {max_runs}\nMin runs: {min_runs}")
    data_of_runs.append([id_sim, mean_runs, np.median(np.array(number_of_runs)), max_runs, min_runs])
    """
    plt.hist(number_of_runs, bins=100)
    plt.xlabel(f'Number of runs')
    plt.ylabel('Frequency')
    plt.title(f'Distribution of number of runs for {id_sim}')
    plt.show()
    """
    reset()


num_of_sims = 1000
seed(20)
data_of_runs = [["min_prob", "Average", "Median", "Max", "Min"]]
simulate(num_of_sims, 0.01, "0.01 Probabilistic range 0-20")
simulate(num_of_sims, 0.01, "0.01 Probabilistic range 10-20", min_range=10, max_range=20)
simulate(num_of_sims, 0.01, "0.01 Probabilistic range 0-50", min_range=0, max_range=50)
simulate(num_of_sims, 0.01, "0.01 Probabilistic range 5-50", min_range=5, max_range=50)
simulate(num_of_sims, 0.01, "0.01 Probabilistic range 15-50", min_range=15, max_range=50)
# simulate(num_of_sims, 0.01, "0.01 Fixed 5", fixed=True, fixed_x=5, fixed_y=5)
# simulate(num_of_sims, 0.01, "0.01 Fixed 10", fixed=True, fixed_x=10, fixed_y=10)
# simulate(num_of_sims, 0.01, "0.01 Fixed 20", fixed=True, fixed_x=20, fixed_y=20)

simulate(num_of_sims, 0.05, "0.05 Probabilistic range 0-20")
simulate(num_of_sims, 0.05, "0.05 Probabilistic range 10-20", min_range=10, max_range=20)
simulate(num_of_sims, 0.05, "0.05 Probabilistic range 0-50", min_range=0, max_range=50)
simulate(num_of_sims, 0.05, "0.05 Probabilistic range 5-50", min_range=5, max_range=50)
simulate(num_of_sims, 0.05, "0.05 Probabilistic range 15-50", min_range=15, max_range=50)
# simulate(num_of_sims, 0.05, "0.05 Fixed 5", fixed=True, fixed_x=5, fixed_y=5)
# simulate(num_of_sims, 0.05, "0.05 Fixed 10", fixed=True, fixed_x=10, fixed_y=10)
# simulate(num_of_sims, 0.05, "0.05 Fixed 20", fixed=True, fixed_x=20, fixed_y=20)

simulate(num_of_sims, 0.10, "0.10 Probabilistic range 0-20")
simulate(num_of_sims, 0.10, "0.10 Probabilistic range 10-20", min_range=10, max_range=20)
simulate(num_of_sims, 0.10, "0.10 Probabilistic range 0-50", min_range=0, max_range=50)
simulate(num_of_sims, 0.10, "0.10 Probabilistic range 5-50", min_range=5, max_range=50)
simulate(num_of_sims, 0.10, "0.10 Probabilistic range 15-50", min_range=15, max_range=50)
# simulate(num_of_sims, 0.10, "0.10 Fixed 5", fixed=True, fixed_x=5, fixed_y=5)
# simulate(num_of_sims, 0.10, "0.10 Fixed 10", fixed=True, fixed_x=10, fixed_y=10)
# simulate(num_of_sims, 0.10, "0.10 Fixed 20", fixed=True, fixed_x=20, fixed_y=20)

simulate(num_of_sims, 0.15, "0.15 Probabilistic range 0-20")
simulate(num_of_sims, 0.15, "0.15 Probabilistic range 10-20", min_range=10, max_range=20)
simulate(num_of_sims, 0.15, "0.15 Probabilistic range 0-50", min_range=0, max_range=50)
simulate(num_of_sims, 0.15, "0.15 Probabilistic range 5-50", min_range=5, max_range=50)
simulate(num_of_sims, 0.15, "0.15 Probabilistic range 15-50", min_range=15, max_range=50)
# simulate(num_of_sims, 0.15, "0.15 Fixed 5", fixed=True, fixed_x=5, fixed_y=5)
# simulate(num_of_sims, 0.15, "0.15 Fixed 10", fixed=True, fixed_x=10, fixed_y=10)
# simulate(num_of_sims, 0.15, "0.15 Fixed 20", fixed=True, fixed_x=20, fixed_y=20)

simulate(num_of_sims, 0.25, "0.25 Probabilistic range 0-20")
simulate(num_of_sims, 0.25, "0.25 Probabilistic range 10-20", min_range=10, max_range=20)
simulate(num_of_sims, 0.25, "0.25 Probabilistic range 0-50", min_range=0, max_range=50)
simulate(num_of_sims, 0.25, "0.25 Probabilistic range 5-50", min_range=5, max_range=50)
simulate(num_of_sims, 0.25, "0.25 Probabilistic range 15-50", min_range=15, max_range=50)
# simulate(num_of_sims, 0.25, "0.25 Fixed 5", fixed=True, fixed_x=5, fixed_y=5)
# simulate(num_of_sims, 0.25, "0.25 Fixed 10", fixed=True, fixed_x=10, fixed_y=10)
# simulate(num_of_sims, 0.25, "0.25 Fixed 20", fixed=True, fixed_x=20, fixed_y=20)

custom_print(data_of_runs)

import openpyxl

# create a new workbook
workbook = openpyxl.Workbook()

# select the active worksheet
worksheet = workbook.active

# write the data to the worksheet
for row in data_of_runs:
    worksheet.append(row)

workbook.save('data_output/mydata2.xlsx')


def move_no_fixed(center, min_step_size=0, max_step_size=20):
    move_by_x = uniform_round(min_step_size, max_step_size)
    move_by_y = uniform_round(min_step_size, max_step_size)
    new_x = round(center[0] + (move_by_x * choice([1, -1])), 4)
    new_y = round(center[1] + (move_by_y * choice([1, -1])), 4)
    return new_x if 0.0 + building_dims[0] // 2 <= new_x <= corners[2] - building_dims[0] // 2 else center[0], \
           new_y if 0.0 + building_dims[1] // 2 <= new_y <= corners[2] - building_dims[1] // 2 else center[1]
