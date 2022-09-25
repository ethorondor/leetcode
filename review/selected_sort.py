'''
sort an array in place
'''
def selected_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        min_number = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < min_number:
                min_index = j
                min_number = arr[j]
        # swap
        _tmp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = _tmp
    return arr
arr = [-9,20,7,2,1]
selected_sort(arr)