'''
smallest subarry with a greated sum
'''
#%%
import math
class solutions:
    def smallest_subarray(self, nums, target):
        ans = []
        l = 0
        _sum = nums[0]
        _len = math.inf
        r = 0
        while r < len(nums)-1:
            if _sum < target:
                r += 1
                _sum = _sum + nums[r]
            else:
                if r - l + 1 < _len:
                    _len = r - l +1
                    ans = nums[l:r+1]
                _sum = _sum - nums[l]
                l += 1
        return ans
 
nums = [2,1,5,2,3,2]
target = 7   
s = solutions()
s.smallest_subarray(nums, target)
# %%
