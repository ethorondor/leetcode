'''
find the k th smallest number
'''
#%%
from heapq import *
def kth_smallest_number(nums, k):
    max_heap = []
    heapify(max_heap)
    for i in range(k):
        heappush(max_heap, -nums[i])
    for j in range(k, len(nums)):
        if -nums[j] > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[j])
    return -max_heap[0]

nums = [1,6,8,2,6,3]
k = 3
h = kth_smallest_number(nums, k)
# %%
