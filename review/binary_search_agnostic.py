'''
binary search agnostic
'''
#%%
class solutions:
    def binary_search_agnostic(self, nums, target):
        if nums[-1] > nums[0]:
            ascending = True
        else:
            ascending = False
        l = 0
        r = len(nums)-1
        while l < r:
            mid =l+ (r-l)//2
            if ascending:
                if nums[mid] > target:
                    r = mid-1
                if nums[mid] < target:
                    l = mid +1
                else:
                    return mid
            else:
                if nums[mid] > target:
                    l = mid+1
                if nums[mid] < target:
                    r = mid-1
                else:
                    return mid
nums = [1,4,6,8,9, 10]
target = 10
s = solutions()
s.binary_search_agnostic(nums, target)
# %%
