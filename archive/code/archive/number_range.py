'''
number range
'''
#%%
def number_range(nums, key):
    l = 0 
    r = len(nums) - 1
    while l < r:
        if key > nums[l] or key < nums[r]:
            if key > nums[l]:
                l += 1
            if key < nums[r]:
                r -= 1
        else:
            return [l,r]
nums = [1,6,6,6,9]
key = 6
number_range(nums, key)
# %%
