from collections import deque
from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    queue = deque()
    fresh_oranges = 0
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh_oranges += 1

    cur_min = 0
    while queue:
        i, j, cur_min = queue.popleft()

        # Up
        if i != 0 and grid[i - 1][j] == 1:
            grid[i - 1][j] = 2
            queue.append((i - 1, j, cur_min + 1))
            fresh_oranges -= 1

        # left
        if j != 0 and grid[i][j - 1] == 1:
            grid[i][j - 1] = 2
            queue.append((i, j - 1, cur_min + 1))
            fresh_oranges -= 1

        # Down
        if i != n - 1 and grid[i + 1][j] == 1:
            grid[i + 1][j] = 2
            queue.append((i + 1, j, cur_min + 1))
            fresh_oranges -= 1

        # Right
        if j != m - 1 and grid[i][j + 1] == 1:
            grid[i][j + 1] = 2
            queue.append((i, j + 1, cur_min + 1))
            fresh_oranges -= 1

    return cur_min if fresh_oranges == 0 else -1


orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])
