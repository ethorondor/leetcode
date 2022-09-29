'''
find largest k elements
'''
#%%
from heapq import *
class solutions:
    def find_k_elements(self, nums, k):
        min_heap = []
        for i in range(k):
            heappush(min_heap, nums[i])
        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, nums[i])
        return min_heap
    
nums = [2,5,1,8,9]
k = 3
s = solutions()
s.find_k_elements(nums, k)
# %%
