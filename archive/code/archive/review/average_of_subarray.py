'''
find the average of k subarray
'''
#%%
class solutions:
    def average_of_subarray(self, arr, k):
        sum = 0
        ans = []
        for i in range(k):
            sum += arr[i]
        ans.append(sum/k)
        for i in range(1 , len(arr) - k+1):
            sum = sum - arr[i-1] + arr[i+k-1]
            ans.append(sum/k)
        return ans
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
s = solutions()
s.average_of_subarray(arr, k)
# %%
