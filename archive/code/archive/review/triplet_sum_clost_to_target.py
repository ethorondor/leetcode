'''
triplet sum close to target
'''
#%%
import math
class solutions:
    def _close_to_target(self, nums, target):
        nums.sort()
        diff = math.inf
        for i in range(len(nums)-1):
            l = i+1
            r = len(nums)-1
            _sum = nums[i]+nums[l]+nums[r]
            while l < r:
                if abs(_sum-target) < diff:
                    diff = abs(_sum-target)
                    ans = _sum
                    l += 1
                if nums[i]+nums[l]+nums[r] > target:
                    r -= 1
                elif _sum < target:
                    l += 1
        return ans
nums = [-2,0,1,2]
target = 2
s = solutions()
s._close_to_target(nums, target)
# %%
