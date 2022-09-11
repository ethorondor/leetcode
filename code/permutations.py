'''
permutations
'''
#%%
from collections import deque
def crt_permutations(nums):
    permutations = deque()
    permutations.append([nums[0]])
    for n in range(1, len(nums)):
        num = nums[n]
        permutations_len = len(permutations)
        for _ in range(permutations_len):          
            pre_permutations = permutations.popleft()  
            for i in range(n+1):
                subset = list(pre_permutations)
                subset.insert(i, num)
                permutations.append(list(subset))
    return list(permutations)

nums = [1,2,3,4]
l = crt_permutations(nums)
# %%
