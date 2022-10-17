
#%%
'''
squaring sorted array
'''
import numpy as np
class solutions:
    def squaring_sorted_array(sefl,arr):
        l = 0
        r = len(arr) - 1
        ans = [np.nan]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            if arr[r]**2 >= arr[l]**2:
                ans[i] = arr[r]**2
                r -= 1
            else:
                ans[i] = arr[l]**2
                l += 1
        return ans
    
arr = [-2,-1,0,1,3]
solution = solutions()
solution.squaring_sorted_array(arr)
