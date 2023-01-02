'''
11 container with most water
'''
#%%
from typing import List
class Solutions:
    def max_area_0(self, height: List[int]) -> int:
        # brute force
        res = 0
        for l in range(len(height)):
            for r in range(l+1, len(height)):
                area = (r-l) * min(height[l], height[r])
                res = max(res, area)
        return res
    def max_area_1(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        while l < r:
            area = (r-l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[l]:
                r -= 1
            else:
                r -= 1
        return res
height = [1,8,6,2,5,4,8,3,7]
s = Solutions()
s.max_area_0(height)
s.max_area_1(height)
# %%
