#%%
'''
11 container with most water
'''
class solution:
    def max_area(self, height):
        res = 0
        l, r = 0,len(height)-1

        while l < r:
            area = (r-l)*min(height[l], height[r])
            res = max(res, area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

height = [1,8,6,2,5,4,8,3,7]
solution = solution()
solution.max_area(height)
#%%
'''
167 Two Sum II
'''
class solution:
    def two_sum(self, numbers, target):
        l,r = 0,len(numbers)-1
        while l < r:
            ans = numbers[l] +  numbers[r]
            if ans < target:
                l += 1
            elif ans > target:
                r -= 1
            else:
                return [l,r]
        
numbers = [2,7,11,15]
target = 9
solution = solution()
solution.two_sum(numbers, target)
# %%
