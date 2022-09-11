'''
subsets with duplicates
'''
#%%
def subsets_with_duplicate(nums):
    nums.sort()
    subsets = []
    subsets.append([])
    prev_num = None
    prev_subset_len = None
    for n in nums:
        subsets_len = len(subsets)
        if n == prev_num:
            l = prev_subset_len
        else:
            l = 0
            prev_subset_len = subsets_len
        for i in range(l, subsets_len):
            s = list(subsets[i])
            s.append(n)
            subsets.append(s)
        # update prev num
        prev_num = n
    return subsets
            
nums = [1,3,3,3,5]
l = subsets_with_duplicate(nums)
# %%
