'''
group same numbers
'''
#%%
from collections import defaultdict
class solutions:
    def group_nums(self, nums):
        res = defaultdict(list)
        for n in nums:
            if n not in res.keys():
                res[n] = []
            res[n].append(n)
        return res.values()
nums = [1,1,1,4,4,5,5]
solution = solutions()
solution.group_nums(nums)
# %%
