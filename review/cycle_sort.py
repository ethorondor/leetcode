'''
cycle sort
'''
class solutions:
    def cycle_sort(self, nums):
        i = 0
        while i < len(nums)-1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                _tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = _tmp
            else:
                i+=1
        return nums
nums = [1,3,2,5,4]
s = solutions()
s.cycle_sort(nums)