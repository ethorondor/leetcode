'''
pair with target sum
'''
#%%
class solutions:
    def pair_target_sum(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] > target:
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                return [nums[l],nums[r]]
nums = [1,2,3,4,5,6]
target = 6
s = solutions()
s.pair_target_sum(nums, target)
# %%
