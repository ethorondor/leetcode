'''
167 two sum II:
given a i-indexed array of integers that is sorted. find two numbers such that they add up to a target.
'''
#%%
from typing import List
class solutions:
    def two_sum_II(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            _sum = numbers[l] + numbers[r]
            if _sum < target:
                l += 1
            elif _sum > target:
                r -= 1
            else:
                return [l+1, r+1]

numbers = [1,3,4,5,7,11]
target = 9
s = solutions()
s.two_sum_II(numbers, target)
# %%
