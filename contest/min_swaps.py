from numpy import argsort
nodes = [7, 6, 8, 5]
nodes = [4, 1, 2, 3]
visited = [False] * len(nodes)
min_l = min(nodes)
swap_count = 0
for i, node in enumerate(nodes):
    if i == node - min_l:
        visited[i] = True
        continue

    j = nodes[i] - min_l
    while not visited[j]:
        swap_count += 1
        j = nodes[j] - min_l
        visited[j] = True

print(swap_count)
print(argsort([7,3,4,1]))


