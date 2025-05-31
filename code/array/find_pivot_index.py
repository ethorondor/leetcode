'''
724 find pivot index
'''
#%%
class Solutions:
    def pivot_index(self, nums):
        for i in range(len(nums)):
            if i == 0:
                if sum(nums[1:]) == 0:
                    return i
            if i < len(nums)-1: 
                if sum(nums[:i]) == sum(nums[i+1:]):
                    return i 
            if i == len(nums) -1:
                if sum(nums[:len(nums)-1]) == 0:
                    return i
        return -1
nums = [1,7,3,6,5,6]
sln = Solutions()
sln.pivot_index(nums)
# %%
