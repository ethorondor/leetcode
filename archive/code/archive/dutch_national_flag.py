'''
dutch national flat
'''
#%%
class solutions:
    def dutch_flag_sort(self, arr):
        l = 0
        h = len(arr) - 1
        i = 0
        while i <= h:
            if arr[i] == 0:
                # swap i with l
                _tmp = arr[l]
                arr[l] = arr[i]
                arr[i] = _tmp
                i += 1
                l += 1
            elif arr[i] == 1:
                i += 1
            elif arr[i] == 2:
                _tmp = arr[h]
                arr[h] = arr[i]
                arr[i] = _tmp
                h -= 1
        return arr
                
arr = [2,2,0,1,2,0]
solution = solutions()
solution.dutch_flag_sort(arr)   
#%%
class solutions:
    def dutch_flag_sort(self, arr):
        flag_freq = {0:0,1:0,2:0}
        res = []
        for i in range(len(arr)):
            flag_freq[arr[i]] += 1
        for key in flag_freq:
            for i in range(flag_freq[key]):
                res.append(key)
        return res
        
arr = [2,2,0,1,2,0]
solution = solutions()
solution.dutch_flag_sort(arr)
# %%
