'''
year book
'''
#%%
def find_sig_counts(arr):
    ans = [1]*len(arr)
    target = list(range(1,len(arr)+1))    
    arr_copy = arr.copy()
    while arr_copy != target:
        for i in range(len(arr)):
            if arr_copy[i] == i + 1:
                pass
            else:
                arr_copy[i] = arr[arr[i]-1]
                ans[i] += 1
    return ans

arr = [2,1]
find_sig_counts(arr)
# %%
