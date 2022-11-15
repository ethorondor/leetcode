'''
1. two sum
given a array of integers nums and an integer target, return indicies of the two numbers that they add up to target.
'''
#%%
from typing import List
class solutions:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # {val: index}
        hash_map = {}
        for ind, val in enumerate(nums):
            diff = target - val
            if diff in hash_map:
                return ([ind, hash_map[diff]])
            hash_map[val] = ind
        return
    
nums = [1,5,3,6]
target = 9
sln = solutions()
sln.two_sum(nums, target)        
# %%
