'''
find top k numbers
'''
#%%
from heapq import *
def top_k_numbers(nums, k):
    min_heap = []
    for i in range(k):
        heappush(min_heap, nums[i])
    for j in range(k ,len(nums)):
        if nums[j] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, nums[j])
    return min_heap
        
nums = [1,3,7,2,9]
k = 3
top_k_numbers(nums, k)        
# %%
