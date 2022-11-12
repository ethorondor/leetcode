'''
kth largest element
'''
from heapq import *
class kth_largest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        self.k = k
        heapq.heapify(self.min_heap)
        while len(len(min_heap)) > k:
            heapq.heappop(self.min_heap)
            
    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(min_heap) > self.k:
            heapq.heappop(min_heap)
        return self.min_heap[0]