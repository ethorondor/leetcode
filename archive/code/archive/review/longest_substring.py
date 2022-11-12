'''
longest substring with unique characters
'''
#%%
class solutions:
    def longest_substring(self, s):
        l = 0
        ans = 0
        sub_string = {}
        for r in range(len(s)):
            if s[r] not in sub_string:
                sub_string[s[r]] = 0
            sub_string[s[r]] += 1
            while sub_string[s[r]] > 1:
                sub_string[s[l]] -= 1
                if sub_string[s[l]] == 0:
                    del sub_string[s[l]]
                l += 1
            ans = max(ans, (r-l+1))
        return ans
s = 'aabbabcc'
solution = solutions()
solution.longest_substring(s)
# %%
