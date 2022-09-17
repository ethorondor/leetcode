'''
3sum
'''
class solutions:
    def three_sum(self, nums):
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            target = 0 - nums[i]
            l = i + 1
            r = len(nums)-1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    if [nums[i],nums[l],nums[r]] not in ans:
                        ans.append([nums[i],nums[l],nums[r]])
                    l += 1
        return ans
nums = [-1,0,1,2,-1,-4]
s = solutions()
s.three_sum(nums)