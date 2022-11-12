'''
rotary lock
'''
#%%
def get_min_code_entry(N,M,C):
    curr = 1
    res = 0
    for i in range(M):
        nxt = C[i]
        if nxt > curr:
            res += min((curr + N - nxt), nxt - curr)
        elif curr > nxt:
            res += min(curr-nxt, N + nxt -curr)
        else:
            res += 0
        curr = C[i]
    return res

N = 10
M = 4
C = [9,4,4,8]
get_min_code_entry(N,M,C)
# %%
