'''
valid palindrome
'''
#%%
class solutions:
    def is_palindromw(self, s):
        new_str = ''
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        return new_str == new_str[::-1]

    def is_palindrome(self, s):
        l = 0
        r = len(s) - 1
        while l <= r:
            while not s[l].isalnum():
                l += 1
            while not s[r].isalnum():
                r -= 1
            if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
            else:
                return False
        return True
    
    
        
s = "A man, a plan, a canal: Panama"
solution = solutions()
#solution.is_palindromw(s)
solution.is_palindrome(s)
# %%
