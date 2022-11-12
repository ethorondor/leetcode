'''
cafeteria
'''
#%%
from typing import List
class solutions:
    def cafeteria(self, N,K,M,S):
        S.sort()
        l = S[0]
        ans = 0
        while l - (K+1) > 0:
            ans += 1
            l = l-(K+1)
        l = S[-1]
        while l + (K+1) <= N:
            ans += 1
            l = l + K+1
        for i in range(len(S)-1):
            l = S[i]
            r = S[i+1]
            while r - l >= 2*K+2:
                ans += 1
                l = l + K+1
        
        return ans
N = 10
M = 3
K = 1
S = [2, 6]
solution = solutions()
solution.cafeteria(N,K,M,S)
# %%
