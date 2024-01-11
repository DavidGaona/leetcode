from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        count = 1
        for digit in digits:
            count *= 3 if digit != "7" and digit != "9" else 4
        ans = [""] * count
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
                   "7": "pqrs", "8": "tuv", "9": "wxyz"}

        next_div = count
        for digit in digits:
            j = 0
            divisor = 3 if digit != "7" and digit != "9" else 4
            k = (next_div // divisor)

            for i in range(count):
                ans[i] += letters[digit][j % divisor]
                if i == (k * (j + 1)) - 1:
                    j += 1
            next_div = k

        return ans


sol = Solution()
sol.letterCombinations("234")
