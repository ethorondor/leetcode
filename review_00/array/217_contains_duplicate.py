'''
given an integer nums, return true if any value appears at least twice in the array and return false if every element is distinct
'''
#%%
from typing import List
class solutions:
    def contain_duplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
nums = [1,3,4,1]
sln = solutions()
sln.contain_duplicate(nums)
# %%
