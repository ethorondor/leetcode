'''
top k frequent element
'''
#%%
from heapq import *
class solutions:
    def top_k_frequent_elements(self, nums, k):
        freq_map = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            if n not in freq_map:
                freq_map[n] = 0
            freq_map[n] += 1
            
        for n, f in freq_map.items():
            freq[f].append(n)
                
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
nums = [1,5,0,5,0,5]
s = solutions()
ans = s.top_k_frequent_elements(nums,k = 2)
# %%
