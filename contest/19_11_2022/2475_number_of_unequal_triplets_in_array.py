from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        num_of_triplets = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if nums[i] != nums[j]:
                    for k in range(j + 1, n):
                        if nums[j] != nums[k] and nums[k] != nums[i]:
                            num_of_triplets += 1

        return num_of_triplets
