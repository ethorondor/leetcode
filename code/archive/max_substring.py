
#%%
import math
class solution:
    def min_size_subarray_sum(self, s, arr):
        l = 0
        min_size = math.inf
        window_sum = 0.0
        for r in range(len(arr)):
            window_sum += arr[r]
            while window_sum > s:
                min_size = min(min_size, r-l+1)
                window_sum -= arr[l]
                l += 1
        if min_size == math.inf:
            min_size = 0
        return min_size
s = 7
arr = [2,1,5,2,8]
solution = solution()
solution.min_size_subarray_sum(s,arr)
#%%
class solution:
    def sliding_window(self, k, arr):
        l = 0
        window_sum = 0.0
        for r in range(len(arr)):
            if r < k:
                window_sum += arr[r]
            else:
                window_sum += arr[r]
                window_sum -= arr[l]
                l+=1
        return window_sum

k = 3
arr = [1,3,5,2,7]
solution = solution()
solution.sliding_window(k,arr)
#%%
'''
smallest subarray with a greater sum
'''
import math
from unittest import result
class solution:
    def min_size_subarray_sum(self,s,arr):
        window_sum = 0
        window_start = 0
        result = math.inf
        for window_end in range(len(arr)):
            window_sum += arr[window_end]
            while window_sum > s:
                result = min(result, window_end-window_start+1)
                window_sum -= arr[window_start]
                window_start += 1
        return result
s = 7
arr = [2,1,5,2,8]
solution = solution()
solution.min_size_subarray_sum(s,arr)
