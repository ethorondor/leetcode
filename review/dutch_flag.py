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
    
    def dutch_flag_one_pass(self, arr):
        l = 0
        h = len(arr) - 1
        for i in range(1,len(arr)-1):
            if arr[i] == 0:
                _tmp = arr[l]
                arr[l] = arr[i]
                arr[i] = _tmp
                l += 1
            if arr[i] == 2:
                _tmp = arr[h]
                arr[h] = arr[i]
                arr[i] = _tmp
                h -= 1
        return arr
arr = [2,0,1,1,0]
s = solutions()
s.dutch_flag_one_pass(arr)
# %%
