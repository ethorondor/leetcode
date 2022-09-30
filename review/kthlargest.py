'''
kth largest element
'''
#%%
from heapq import *
class kthlargest:
    def __init__(self,k,nums):
        self.k = k
        self.nums = nums
        
    def add(self, val):
        self.nums.append(val)
        max_heap = []
        for i in range(self.k):
            heappush(max_heap, -1*self.nums[i])
        for i in range(self.k, len(self.nums)):
            if max_heap[0] < -1*self.nums[i]:
                heappop(max_heap)
                heappush(max_heap, -1*self.nums[i])
        return -1*max_heap[0]
obj = kthlargest(3,[4,5,8,2])
obj.add(3)
# %%
