'''
inplace sorting
'''
#%%
def inplace_sorting(arr):
    for i in range(len(arr)):
        min_number = arr[i]
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < min_number:
                min_number = arr[j]
                min_index = j
        #swap
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [3,1,6,0,9]
inplace_sorting(arr)
# %%
