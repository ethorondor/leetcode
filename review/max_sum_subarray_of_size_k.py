'''
maximum sum of subarray of size k
'''
class solutions:
    def max_sum_subarray(self, nums, k):
        ans = 0
        # initialize subarray
        sums = 0
        for i in range(k):
            sums += nums[i]