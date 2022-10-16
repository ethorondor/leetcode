'''
longest consecutive sequence
'''
#%%
def longest_consecutive_sequence(arr):
    arr_set = set(arr)
    longest = 0
    for n in arr:
        if n-1 not in arr_set:
            length = 0
            while n+length in arr_set:
                length += 1
            longest = max(longest, length)
    return longest
    
arr = [100, 1, 200, 2, 3, 4]
longest_consecutive_sequence(arr)
# %%
