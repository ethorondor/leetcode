'''
connecting ropes
'''
#%%
from heapq import *
class solutions:
    def connecting_ropes(self, nums):
        min_heap = []
        ans = [0]*(len(nums)+1)
        result = 0
        for i in range(len(nums)):
            heappush(min_heap, nums[i])
        for i in range(1,len(min_heap)+1):
            ans[i] = ans[i-1]+heappop(min_heap)
        for i in range(len(ans)):
            result += ans[i]
        return result
    
nums = [3,1,11,5]
s = solutions()
s.connecting_ropes(nums)
# %%
