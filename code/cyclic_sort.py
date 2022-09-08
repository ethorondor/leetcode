'''
cyclic sort
'''
class solutions:
    def cycle_sort(self, nums):
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                _tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = _tmp
            else:
                i += 1
        return nums
        
nums = [1,5,7,4,3,2]
solution = solutions()
solution.cycle_sort(nums)