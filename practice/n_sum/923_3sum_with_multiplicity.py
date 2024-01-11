from collections import defaultdict
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = 0
        counts = [0] * 101
        for num in arr:
            counts[num] += 1

        for k in range(101):
            if counts[k] == 0:
                continue
            i = k if counts[k] > 1 else k + 1
            j = 100
            while i <= j:
                if counts[i] == 0:
                    i += 1
                    continue

                if counts[j] == 0:
                    j -= 1
                    continue

                res = target - (i + j + k)

                if res == 0:
                    count += min(counts[i], counts[j], counts[k])
                elif res > 0:
                    i += 1
                else:
                    j -= 1

        return count


sol = Solution()
sol.threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8)


class Solution2:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = 0
        counts = [0] * 101
        for num in arr:
            counts[num] += 1

        i = k = 0
        j = 101
        for k in range(101):
            while i <= j:
                if counts[i] == 0:
                    i += 1
                    continue

                if counts[j] == 0:
                    j -= 1
                    continue

                k = target - (i + j)
                if k < i:
                    j -= 1
                    continue

                if k > j:
                    i += 1
                    continue

                if counts[k] == 0:
                    continue

                if k != 0:
                    continue

                counts += min(counts[i], counts[j], counts[k])
