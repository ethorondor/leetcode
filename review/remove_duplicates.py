'''
remove duplicates
'''
#%%
class solutions:
    def remove_duplicates(self, nums):
        l = 0
        r = 1
        while r < len(nums):
            if nums[l] == nums[r]:
                nums.pop(r)
            else:
                l += 1
                r += 1
        return nums
    
nums = [1,4,4,4,6,7,7]
s = solutions()
s.remove_duplicates(nums)
# %%
