'''
koko eats bananas
'''
#%%
import math
class solutions:
    def koko_eats_bananas(self, piles, h):
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            k = l + (r-l)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h:
                res = min(res, hours)
                r = k-1
            else:
                l = k+1
        return k
piles = [3,6,7,11]
h = 8
solution = solutions()
solution.koko_eats_bananas(piles, h)
# %%
