from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for num in nums:
            if num <= 0 or num > n:
                continue

            j = num
            while (0 < j <= n) and j != nums[j - 1]:
                temp = nums[j - 1]
                nums[j - 1] = j
                j = temp

        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1

        return n + 1


sol = Solution()
print(sol.firstMissingPositive([2, 3, 4]))
