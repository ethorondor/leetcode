'''
238. product of array except self
given an integer array of nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]
'''
#%%
class solutions:
    def product_array(self, nums):
        res = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
nums = [1,2,3,4]
sln = solutions()
sln.product_array(nums)
# %%
