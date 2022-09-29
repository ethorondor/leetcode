'''
find the next permutation
'''
#%%
class solutions:
    def next_permutation(self, nums):
        n = len(nums)
        pivot = 0
        for i in range(n-1,0,-1):
            if nums[i-1]<nums[i]:
                pivot = i
                break
        if pivot == 0:
            nums.sort()
            return
        swap = n-1
        while nums[pivot-1] > nums[swap]:
            swap -= 1
        nums[swap],nums[pivot-1] = nums[pivot-1],nums[swap]
        nums[pivot:] = sorted(nums[pivot:])
        return nums
        
nums = [1,2,3,5,4,3,2,1]
sl = solutions()
sl.next_permutation(nums)
# %%
