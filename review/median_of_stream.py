'''
define a class that will return median of a stream
'''
#%%
import heapq
class median_of_stream:
    '''
    initialize your data structure
    '''
    def __init__(self):
        # two heaps minheap maxheap
        self.minheap = []
        self.maxheap = []
    
    def insert(self, num):
        heapq.heappush(self.minheap, -1*num)
        # make sure every number is minheap is smaller than that in maxheap
        if (self.minheap and self.maxheap and self.minheap[0]*(-1) > self.maxheap[0]):
            val = -1 * heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, val)
        if (len(self.minheap) > len(self.maxheap)+1):
            val = -1 * heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, val)
        if (len(self.minheap) +1 < len(self.maxheap)):
            val = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -1*val)
            
    def find_median(self):
        if len(self.minheap) > len(self.maxheap):
            return -1*self.minheap[0]
        if len(self.maxheap) > len(self.minheap):
            return self.maxheap[0]
        return (-1*self.minheap[0]+self.maxheap[0])/2
    
s = median_of_stream()
s.insert(1)
s.insert(2)
s.insert(5)
s.insert(4)
s.find_median()
# %%
