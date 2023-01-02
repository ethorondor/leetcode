'''
125 valid palindrome
A phase is a palindrome if after converting all uppercase letters to lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
'''
#%%
class solutions:
    def valid_palindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
    def valid_palindrome_alt_1(self, s: str) -> bool:
        new_str = ''
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        return new_str == new_str[::-1]
    
   
        

s = 'A man, a Plan, a canal: Panama'
sln = solutions()
sln.valid_palindrome(s)
# %%
