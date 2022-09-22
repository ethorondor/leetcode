'''
dutch flag
'''
#%%
class solutions:
    def dutch_flag(self, arr):            
        for i in range(1,len(arr)):
            j = i
            while (j-1) in range(len(arr)) and arr[j-1] > arr [j]:
                    _tmp = arr[j-1]
                    arr[j-1] = arr[j]
                    arr[j] = _tmp
                    j -= 1
                 
        return arr
arr = [2,0,1,1,0]
s = solutions()
s.dutch_flag(arr)
# %%
