'''
238. product of array except self
given an integer array of nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]
'''
#%%
class solutions:
    def product_array(self, nums):
        res = [1]*len(nums)
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        ans = 1
        for i in range(len(nums)):
            prefix[i] = ans
            ans *= nums[i]
        ans = 1
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = ans
            ans *= nums[i]
        for i in range(len(nums)):
            res[i] = prefix[i]*postfix[i]
        return res
nums = [1,2,3,4]
sln = solutions()
sln.product_array(nums)
# %%
