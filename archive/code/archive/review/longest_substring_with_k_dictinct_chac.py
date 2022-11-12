'''
longest substring with k distinct characters
'''
#%%
import math
class solutions:
    def longest_substring(self, str, k):
        l = 0
        r = 1
        str_set = {}
        max_len = 0
        for r in range(len(str)):
            if str[r] not in str_set:
                str_set[str[r]] = 0
            str_set[str[r]] += 1
            if len(str_set) <= k:
                max_len = max(max_len, r-l+1)
                ans = str[l:r+1]
            while len(str_set) >k:
                str_set[str[l]] -= 1
                if str_set[str[l]] == 0:
                    str_set.pop(str[l])
                l += 1
                
        return ans
str = 'arraci'
k = 2
s = solutions()
s.longest_substring(str, k)
# %%
