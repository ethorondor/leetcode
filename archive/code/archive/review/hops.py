'''
hops
'''
#%%
def hops(n, f, p):
    _path = {i:0 for i in range(n)}
    for i in p:
        _path[i-1] += 1
    l = 0
    r = 1
    ans = 0
    while l < n-1 and r <= n-1:
        if _path[l] == 0:
            l += 1
            r += 1
        elif _path[l] == 1 and _path[r] == 0 and r < n:
            ans += 1
            _path[l], _path[r] = _path[r], _path[l]
            l += 1
            if r == n-1:
                _path[r] = 0
                r -= 1
            elif r < n-1:    
                r += 1
        elif _path[l] == 1 and _path[r] == 1:
            r += 1     
    return ans

n = 6
f = 3
p = [5,2,4]
hops(n,f,p)
# %%
