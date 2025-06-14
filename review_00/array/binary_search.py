# 704 binary search
#%%
class Solution:
    def binary_search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
nums = [1, 4, 7, 9, 10, 56]
target = 7
sln = Solution()
result = sln.binary_search(nums, target)
print(result)  # Output: 2 (index of target in nums)
# %%
