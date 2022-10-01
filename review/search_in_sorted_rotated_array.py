'''
search in rotated sorted array
'''
#%%
class solutions:
    def search_in_rotated_sorted_array(self, nums, target):
        l = 0
        r = len(nums) - 1
        if nums[0] == target:
            return 0
        if nums[r] == target:
            return r
        m = (l+r)//2
        if nums[m] > nums[l]:
            while nums[m+1] > nums[m]:
                m += 1
        elif nums[m] < nums[l]:
            while nums[m] < nums[m+1]:
                m -= 1
        if target == nums[l]:
            return l
        if target > nums[l]:
            l = 0
            r = m
        else:
            l = m+1
            r = len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if target < nums[mid]:
                r = mid-1
            elif target > nums[mid]:
                l = mid+1
            else:
                return mid
        return -1
nums = [1,3]
k = 3
s = solutions()
s.search_in_rotated_sorted_array(nums, k)
# %%
