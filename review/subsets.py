'''
find all subsets
'''
#%%
class solutions:
    def subsets(self, nums):
        subset = []
        subset.append([])
        for n in nums:
            l = len(subset)
            for i in range(l):
                s = subset[i].copy()
                s.append(n)
                subset.append(s)
        return subset
nums = [0,1,2,3]
s = solutions()
s.subsets(nums)
# %%
