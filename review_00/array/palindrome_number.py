# 9 panlindrome number 
#%%
class Solution:
    def is_palindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        l, r = 0, len(str_x) - 1
        while l <= r:
            if str_x[l] != str_x[r]:
                return False
            l += 1
            r -= 1
        return True
x = 121
sln = Solution()
print(sln.is_palindrome(x))  # Output: True
# %%
