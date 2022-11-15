'''
49. group anagrams
given an array of strings strs, group the anagrams together. 
'''
#%%
from collections import defaultdict
from typing import List
class solutions:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict is a subclass of dict, it will not raise key error when key value is not present, it provide default value for the key that does not exist.
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # count is a list, it can not be keys of a dictionary, change to tuple which is immutable
            res[tuple(count)].append(s)
        return res.values()
    
strs = ['eat','tea','ate','nat','bat','bta']
sln = solutions()
sln.group_anagrams(strs)
# %%
