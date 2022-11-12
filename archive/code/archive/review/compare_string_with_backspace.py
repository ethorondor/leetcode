'''
compare string with backspace
'''
#%%
from collections import deque
class solutions:
    def compare_string(self, str1, str2):
        def crt_q(s):
            q = deque()
            for i in range(len(s)):
                if s[i] == '#':
                    q.pop()
                else:
                    q.append(s[i])
            return q
        return crt_q(str1) == crt_q(str2)
            
str1 = 'xyy#'
str2 = 'xz#y'
solution = solutions()
solution.compare_string(str1,str2)
# %%
