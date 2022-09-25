'''
missing number
'''
#%%
class solutions:
    def missing_number(self, nums):
        i = 0
        while i < len(nums)-1:
            j = nums[i]
            if nums[i] < len(nums) and nums[i] != nums[j]:
                _tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = _tmp
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i:
                return i

nums = [4,0,3,1]
s = solutions()
s.missing_number(nums)
# %%
