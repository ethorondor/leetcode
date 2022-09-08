'''
find all missing numbers
we are given an unsorted array containing numbers from range 1 to n, the array can have duplicates, which means some numbers are missing. Find all missing numbers.
'''
#%%
class solutions:
    def find_all_missing_numbers(self, nums):
        res = []
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if j < len(nums) and nums[i] !=  nums[j]:
                _tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = _tmp
            else:
                i += 1
        for i in range(len(nums)-1):
            if nums[i] != i+1:
                res.append(nums[i])
        return res

nums = [1,4,4,5,5]
solution = solutions()
solution.find_all_missing_numbers(nums)
# %%
