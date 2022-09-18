'''
longest substring with k distinct characters
'''
#%%
import math
class solutions:
    def longest_substring(self, str, k):
        l = 0
        r = 1
        substring = []
        substring.append(str[0])
        max_len = 0
        while l < r and r < len(str):
            if str[r] in substring:
                if r - l + 1 > max_len:
                    max_len = r-l+1
                    max_str = str[l:r+1]
                r += 1
            elif str[r] not in substring and len(substring) < k:
                substring.append(str[r])
                if r - l + 1 > max_len:
                    max_len = r-l+1
                    max_str = str[l:r+1]
                r += 1
            elif str[r] not in substring and len(substring) >= k:
                l += 1
                r = l + 1
                substring = []
                substring.append(str[l])

        return max_str
str = 'arraci'
k = 2
s = solutions()
s.longest_substring(str, k)
# %%
