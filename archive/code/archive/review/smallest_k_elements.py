'''
smallest k elements
'''
#%%
from heapq import *
class solutions:
    def smallest_k_elements(self, nums, k):
        min_heap = []
        for i in range(k):
            heappush(min_heap, -1*nums[i])
        for i in range(k, len(nums)):
            if min_heap[0] < -nums[i]:
                heappop(min_heap)
                heappush(min_heap, -1*nums[i])
        return -min_heap[0]
    
nums = [1,6,9,3,6]
k = 3
s = solutions()
ans = s.smallest_k_elements(nums,k)
# %%
