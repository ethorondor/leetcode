'''
longest substring without repeating
'''
#%%
class solutions:
    def longest_substring(self, s):
        substring = set()
        ans = 0
        l = 0
        r = 0
        while r < len(s):
            if str[r] not in substring:
                substring.add(str[r])
                ans = max(ans, len(substring))
            else:
                substring = set()
                l += 1
                r = l
                substring.add(str[r])
            r += 1
        return ans
    
str = 'dvdf'
s = solutions()
s.longest_substring(str)
# %%
