#%%
'''
remove duplicates
'''
def remove_duplicates(arr):
  # index of the next non-duplicate element
    l = 1
    r = 1
    while r < len(arr):
        if arr[r] != arr[r-1]:
            arr[l] = arr[r]
            l += 1
            r += 1
        else:
            r +=1
    return l
arr = [2,2,3,3,3,6,9,9]
remove_duplicates(arr)
