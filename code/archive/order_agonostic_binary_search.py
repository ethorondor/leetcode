'''
order-agonostic binary search
'''
#%%
def binary_search(nums, target):
    l = 0
    r = len(nums)-1
    is_ascending = (nums[l] < nums[r])
    while l < r:
        m = l + (r-l)//2
        if is_ascending:
            if target < nums[m]:
                r = m-1
            elif target > nums[m]:
                l = m+1
            else:
                return m
        else:
            if target <nums[m]:
                l = m+1
            elif target > nums[m]:
                r = m-1
            else:
                return m          
    return None


nums = [1,2,3,4]
binary_search(nums, 3)
# %%
