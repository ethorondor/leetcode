'''
find all missing numbers
'''
#%%
class solutions:
    def find_all_missing_numbers(self, nums):
        i = 0
        while i < len(nums):
            j = nums[i]-1
            if nums[i] != nums[j]:
                _tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = _tmp
            else:
                i += 1
        missing = []
        for i in range(len(nums)):
            if nums[i]!=i+1:
                missing.append(i+1)
        return missing
    
nums = [5,4,4,3,5]
s = solutions()
s.find_all_missing_numbers(nums)
# %%
