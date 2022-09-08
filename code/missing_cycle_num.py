'''
missing cycle numbers
'''
#%%
class solutions:
    def missing_cycle_nums(self, nums):
        i = 0
        while i < len(nums):
            j = nums[i]
            if nums[i]< len(nums) and nums[i] != nums[j]:
                _tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = _tmp
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i:
                return (i)
        return None
    
nums = [4,0,3,1]
solution = solutions()
solution.missing_cycle_nums(nums)
# %%
