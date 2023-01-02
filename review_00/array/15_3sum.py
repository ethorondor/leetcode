'''
15 3 sum
'''
#%%
from typing import List 
class solutions:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                _three_sum = a + nums[l] + nums[r]
                if _three_sum < 0:
                    l += 1
                elif _three_sum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return res 
    
nums = [-1, 0, 1, 2, -1, -4]
s = solutions()
s.three_sum(nums)
# %%
