from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for ind, value in enumerate(nums):
            if value not in hash_table:
                hash_table[target - value] = ind
            else:
                ind_1 = hash_table[value]
                return [ind_1, ind]
