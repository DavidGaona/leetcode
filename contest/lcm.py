from math import lcm
from typing import List


def subarrayLCM(self, nums: List[int], k: int) -> int:
    n = len(nums)
    count = 0

    low = 0
    has_carry = False

    for num, i in enumerate(nums):
        if lcm(nums[low::i]) == k:
            count += 1

