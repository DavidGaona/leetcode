from collections import deque
from typing import List

from numpy import argsort


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ans = [0] * len(queries)
        n = len(grid)
        m = len(grid[0])
        sorted_queries = sorted(queries)
        sorted_indexes = argsort(queries)
        moves = deque()
        visited = set()
        cur_count = 0
        final_moves = deque()
        final_moves.append([0, 0, True])
        for k, query in enumerate(sorted_queries):
            # Append past edge moves
            for move in final_moves:
                moves.append(move)
            final_moves = deque()
            while len(moves) > 0:
                i, j, is_edge = moves.pop()

                if f"{i},{j}" in visited and not is_edge:
                    continue

                if grid[i][j] < query:
                    if f"{i},{j}" not in visited:
                        cur_count += 1
                    if i != 0:
                        moves.append([i - 1, j, False])

                    if i != (n - 1):
                        moves.append([i + 1, j, False])

                    if j != 0:
                        moves.append([i, j - 1, False])

                    if j != (m - 1):
                        moves.append([i, j + 1, False])
                    visited.add(f"{i},{j}")
                else:
                    final_moves.append([i, j, True])

            ans[sorted_indexes[k]] = cur_count

        return ans


sol = Solution()
print(sol.maxPoints([[1, 2, 3], [2, 5, 7], [3, 5, 1]], [5, 6, 2]))

from collections import deque

uwu = deque([1, 2, 3])

