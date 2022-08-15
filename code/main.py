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
