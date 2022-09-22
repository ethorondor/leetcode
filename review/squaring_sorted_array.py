'''
squaring a sorted array
'''
#%%
class solutions:
    def squaring_sorted_array(self, nums):
        ans = []
        l = 0
        r = len(nums) - 1
        while l <= r:
            l_square = nums[l]**2
            r_square = nums[r]**2
            if l_square < r_square:
                ans.insert(0,r_square)
                r -= 1
            elif l_square >= r_square:
                ans.insert(0,l_square)
                l += 1
        return ans
nums = [-2,-1,0,2,3,4]
s = solutions()
s.squaring_sorted_array(nums)                    
# %%
