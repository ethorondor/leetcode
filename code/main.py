#%%
'''
424 longest repeating character replacement
'''
class solution:
    def character_replacement(self, s, k):
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0) # get the count of s[r], if no, return 0
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
s = "AABABBA"
k = 2
solution = solution()
solution.character_replacement(s,k)
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
