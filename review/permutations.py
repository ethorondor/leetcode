'''
permutations
'''
#%%
from collections import deque
class solutions:
    def permutations(self, nums):
        ans = []
        permutations = deque()
        permutations.append([])
        for i in nums:
            n = len(permutations)
            for _ in range(n):
                pre = permutations.popleft()
                for j in range(len(pre)+1):
                    new = list(pre)
                    new.insert(j,i)
                    if len(new) == len(nums):
                        ans.append(new)
                    else:
                        permutations.append(new)
        return ans
    
nums = [3,1,5]
s = solutions()
s.permutations(nums)
# %%
