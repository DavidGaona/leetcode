from numpy import argsort


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        mem = {}
        steps = [0] * (hi - lo + 1)
        for i in range(lo, hi + 1):
            val = i
            counter = 0
            stop_at = 1
            while val != 1:
                if val in mem:
                    counter += mem[val]
                    stop_at = val
                    break
                if val % 2 == 0:
                    val = val // 2
                else:
                    val = (3 * val) + 1
                counter += 1
            steps[i - lo] = counter
            val = i
            for j in range(counter, -1, -1):
                if val == 1 or val == stop_at:
                    break
                mem[val] = j
                if val % 2 == 0:
                    val = val // 2
                else:
                    val = (3 * val) + 1

        return argsort(steps, kind='stable')[k - 1] + lo
