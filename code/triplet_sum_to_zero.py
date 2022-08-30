'''
triplet sum to zero
'''
#%%
class solutions:
    def triplet_sum_to_zero(self, arr):
        res = []
        arr.sort()
        for i,a in enumerate(arr):
            if i > 0 and a == arr[i-1]:
                continue
            l = i+1
            r = len(arr) - 1
            while l < r:
                sums = a + arr[l] + arr[r]
                if sums > 0:
                    r -= 1
                elif sums < 0:
                    l += 1
                else:
                    res.append([a,arr[l],arr[r]])
                    l += 1
                    while arr[l] == arr[l-1] and l<r:
                        l+=1
        return res
            
arr = [-1,0,1,2,-1,-4]
solution = solutions()
solution.triplet_sum_to_zero(arr)
# %%
