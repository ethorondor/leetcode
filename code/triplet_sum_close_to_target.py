'''
triplet sum close to target
'''
#%%
import numpy as np
class solutions:
    def triplet_sum_closet(self, arr, target):
        arr.sort()
        ans = np.inf
        for i, num in enumerate(arr):
            l = i +1
            r = len(arr)-1
            while l < r:
                diff = num + arr[l] + arr[r] - target
                if abs(diff) < ans:
                    ans = min(abs(diff),ans)
                    res = num + arr[l] + arr[r]
                l += 1
        return res
                
arr = [4,0,5,-5,3,3,0,-4,-5]
target = -2
solution = solutions()
solution.triplet_sum_closet(arr, target)
# %%
