'''
triplet sum to zero
'''
#%%
class solutions:
    def triplet_sum_to_zero(self, nums):
        nums.sort()
        ans = []
        for i in range(len(nums)):
            l = i+1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    if [nums[i],nums[l],nums[r]] not in ans:
                        ans.append([nums[i],nums[l],nums[r]])
                    l += 1
        return ans
nums = [-3,0,1,2,-1,1,-2]
s = solutions()
s.triplet_sum_to_zero(nums)
# %%
