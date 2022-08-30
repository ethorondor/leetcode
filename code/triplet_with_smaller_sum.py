'''
triplets with smaller sum
'''
#%%
class solutions:
    def triplet_with_smaller_sum(self, arr, target):
        ans = 0
        for i,a in enumerate(arr):
            l = i + 1
            r = len(arr) - 1
            while l < r:
                sums = arr[i] + arr[l] + arr[r]
                if sums < target:
                    ans += r-l                    
                    l += 1
                else:
                    r -=1
        return ans
                
        
arr = [-1, 0, 2, 3]
target = 3
solution = solutions()
solution.triplet_with_smaller_sum(arr, target)
# %%
