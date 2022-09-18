'''
maximum sum of subarray of size k
'''
#%%
class solutions:
    def max_sum_subarray(self, nums, k):
        ans = 0
        # initialize subarray
        sums = 0
        for i in range(k):
            sums += nums[i]
        for n in range(k, len(nums)):
            sums = sums + nums[n] - nums[n-k]
            ans = max(ans, sums)
        return ans
nums = [1,4,2,6,9]
k = 2
s = solutions()
s.max_sum_subarray(nums, k)
# %%
