'''
ceiling of a number
'''
#%%
def ceiling(nums, key):
    l = 0
    r = len(nums) - 1
    while l < r:
        if r - l == 1:
            if nums[l] > key:
                return nums[l]
            else:
                return nums[r]
        m = l + (r-l)//2
        if key > nums[m]:
            l = m 
        elif key < nums[m]:
            r = m 
        else: 
            return nums[m]
    return -1

nums = [1,2,3,5,6,8,10]
key = 4
ceiling(nums, key=key)
# %%
