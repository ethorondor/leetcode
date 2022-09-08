'''
find all missing numbers
we are given an unsorted array containing numbers from range 1 to n, the array can have duplicates, which means some numbers are missing. Find all missing numbers.
'''
#%%
class solutions:
    def find_all_missing_numbers(self, nums):
        res = []
        i = 0
        for j in range(len(nums)):
            j = nums[i] - 1
            if j < len(nums) and nums[i] !=  nums[j]:
                _tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = _tmp
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i:
                res.append(i)
        return res

nums = [2, 3, 1, 8, 2, 3, 5, 1]
solution = solutions()
solution.find_all_missing_numbers(nums)
# %%
