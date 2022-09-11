'''
find all subsets
'''
#%%
def find_subsets(nums):
    subset = []
    subset.append([])
    for number in nums:
        len_subset = len(subset)
        for i in range(len_subset):
            set1 = list(subset[i])
            set1.append(number)
            subset.append(set1)
    return subset

nums = [1,3,5]
l = find_subsets(nums)
# %%
