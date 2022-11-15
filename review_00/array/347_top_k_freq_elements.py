'''
347 top k frequent elements
given an integer array nums and an integer k, return k most frequent elements.
'''
#%%
from typing import List
class solutions:
    def top_k_freq_elements(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

nums = [1,1,1,2,2,3,3,4]
k = 3
sln = solutions()
sln.top_k_freq_elements(nums, k)

# %%
