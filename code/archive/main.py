
#%%
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
current = head
current.next.next = None
#%%
'''
squaring sorted array
'''
import numpy as np
class solutions:
    def squaring_sorted_array(sefl,arr):
        l = 0
        r = len(arr) - 1
        ans = [np.nan]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            if arr[r]**2 >= arr[l]**2:
                ans[i] = arr[r]**2
                r -= 1
            else:
                ans[i] = arr[l]**2
                l += 1
        return ans
    
arr = [-2,-1,0,1,3]
solution = solutions()
solution.squaring_sorted_array(arr)
#%%
'''
remove duplicates
'''
def remove_duplicates(arr):
  # index of the next non-duplicate element
    l = 1
    r = 1
    while r < len(arr):
        if arr[r] != arr[r-1]:
            arr[l] = arr[r]
            l += 1
            r += 1
        else:
            r +=1
    return l
arr = [2,2,3,3,3,6,9,9]
remove_duplicates(arr)
#%%
'''
happy number
'''
def happy_num(num):
    slow = num
    fast = num
    while True:
        slow = get_square_sum(slot)
        fast = get_square_sum(get_square_sum(fast))
        if slow == fast:
            break
    return slow == 1
    
    
    
def get_square_sum(num):
    _sum = 0
    while num > 0:
        digit = num%10
        _sum += digit**2
        num //=10
    return _sum
get_square_sum(135)
#%%
'''
longest substring with same letters after replacement
'''
class solution:
    def length_of_longest_substring(self, str1,k):
        l = 0
        max_length = 0
        str_dict = {}
        for r in range(len(str1)):
            if str1[r] not in str_dict:
                str_dict[str1[r]] = 1
            else:
                str_dict[str1[r]]+= 1
            while sum(str_dict.values()) - max(str_dict.values()) >2:
                str_dict[str1[l]] -= 1
                l += 1
                
            max_length = max(max_length, sum(str_dict.values()))
        return max_length
str1 = 'abccde'
solution = solution()
solution.length_of_longest_substring(str1,2)
                
#%%
def non_repeat_substring(str1):
  window_start = 0
  max_length = 0
  char_index_map = {}

  # try to extend the range [windowStart, windowEnd]
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    # if the map already contains the 'right_char', shrink the window from the beginning so that
    # we have only one occurrence of 'right_char'
    if right_char in char_index_map:
      # this is tricky; in the current window, we will not have any 'right_char' after its previous index
      # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
      window_start = max(window_start, char_index_map[right_char] + 1)
    # insert the 'right_char' into the map
    char_index_map[right_char] = window_end
    # remember the maximum length so far
    max_length = max(max_length, window_end - window_start + 1)
  return max_length
str='aabccbb'
non_repeat_substring(str)
'''
longest substring with distinct characters
'''
class solution:
    def non_repeat_substring(self, str):
        l = 0
        sub_str = []
        sub_str_len = 0
        for r in range(len(str)):

            while str[r] in sub_str:
                sub_str.remove(str[l])
                l += 1
            sub_str.append(str[r])
            sub_str_len = max(len(sub_str),sub_str_len)
        return sub_str_len
str = 'abccde'
solution = solution()
solution.non_repeat_substring(str)
#%%
def fruits_into_baskets(fruits):
  window_start = 0
  max_length = 0
  fruit_frequency = {}

  # try to extend the range [window_start, window_end]
  for window_end in range(len(fruits)):
    right_fruit = fruits[window_end]
    if right_fruit not in fruit_frequency:
      fruit_frequency[right_fruit] = 0
    fruit_frequency[right_fruit] += 1

    # shrink the sliding window, until we are left with '2' fruits in the fruit frequency dictionary
    while len(fruit_frequency) > 2:
      left_fruit = fruits[window_start]
      fruit_frequency[left_fruit] -= 1
      if fruit_frequency[left_fruit] == 0:
        del fruit_frequency[left_fruit]
      window_start += 1  # shrink the window
    max_length = max(max_length, window_end-window_start + 1)
  return max_length
fruits_into_baskets(['A','A', 'B', 'C', 'A', 'C'])

def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))

#%%
'''
fruits in baskets
'''
class solution:
    def fruits_into_baskets(self, fruits):
        l = 0
        baskets = {}
        baskets_len = 0
        for r in range(len(fruits)):
            if fruits[r] not in baskets:
                baskets[fruits[r]] = 0
            baskets[fruits[r]] += 1
            
            while len(baskets) > 2:
                baskets[fruits[l]] -= 1
                if baskets[fruits[l]] == 0:
                    baskets.pop(fruits[l])
                l += 1
            baskets_len = max(sum(baskets.values()), baskets_len)
        return baskets_len
            
    
fruits = ['A','A','B','C','B','B','C']
solution = solution()
solution.fruits_into_baskets(fruits)
#%%
'''
find the length of the longest substring in it with no more than k distinct characters
'''
class solution:
    def max_substring(self, k, s):
        l = 0
        string_dict = {}
        max_len = 0
        for r in range(len(s)):
            if s[r] not in string_dict:
                string_dict[s[r]] = 0

            string_dict[s[r]] += 1
            while len(string_dict) >k:
                string_dict[s[l]] -= 1
                if string_dict[s[l]] == 0:
                    string_dict.pop(s[l])
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len 
k = 2
s = 'araaci'
solution = solution()
solution.max_substring(k,s)
#%%
import math
class solution:
    def min_size_subarray_sum(self, s, arr):
        l = 0
        min_size = math.inf
        window_sum = 0.0
        for r in range(len(arr)):
            window_sum += arr[r]
            while window_sum > s:
                min_size = min(min_size, r-l+1)
                window_sum -= arr[l]
                l += 1
        if min_size == math.inf:
            min_size = 0
        return min_size
s = 7
arr = [2,1,5,2,8]
solution = solution()
solution.min_size_subarray_sum(s,arr)
#%%
class solution:
    def sliding_window(self, k, arr):
        l = 0
        window_sum = 0.0
        for r in range(len(arr)):
            if r < k:
                window_sum += arr[r]
            else:
                window_sum += arr[r]
                window_sum -= arr[l]
                l+=1
        return window_sum

k = 3
arr = [1,3,5,2,7]
solution = solution()
solution.sliding_window(k,arr)
#%%
'''
smallest subarray with a greater sum
'''
import math
from unittest import result
class solution:
    def min_size_subarray_sum(self,s,arr):
        window_sum = 0
        window_start = 0
        result = math.inf
        for window_end in range(len(arr)):
            window_sum += arr[window_end]
            while window_sum > s:
                result = min(result, window_end-window_start+1)
                window_sum -= arr[window_start]
                window_start += 1
        return result
s = 7
arr = [2,1,5,2,8]
solution = solution()
solution.min_size_subarray_sum(s,arr)
#%%
'''
smallest subarray with a greater sum
'''
class solution:
    def min_size_subarray_sum(self, s, arr):
        l = 0
        r = 0
        window_sum = arr[0]
        result = []
        while l<r+1 and r < len(arr):
            while window_sum < s:
                r+=1
                if r >= len(arr):
                    return min(result)
                else:
                    window_sum += arr[r]
            if window_sum >=s:
                result.append(r-l+1)
                window_sum -= arr[l]
                l+=1
        return min(result)
                
s = 7
arr = [2,1,5,2,8]
solution = solution()
solution.min_size_subarray_sum(s,arr)
                
#%%
'''
853 car fleet
'''
class solution:
    def car_fleet(self, target, position, speed):
        pair = [[p,s] for p,s in zip(position, speed)]
        stack = []
        for p,s in sorted(pair)[::-1]: # reverse sorted order
            stack.append((target-p)/s) 
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
target = 10
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
solution = solution()
solution.car_fleet(target, position, speed)
#%%
'''
739 daily temperatures
'''
class solution:
    def daily_temperatures(self, temperatures):
        res = [0]*len(temperatures)
        stack = []
        
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stack_t, stack_ind = stack.pop()
                res[stack_ind] = (i-stack_ind)
            stack.append([t, i])
        return res
temperatures = [73,74,75,71,69,72,76,73]
solution = solution()
solution.daily_temperatures(temperatures)
#%%
'''
155 min stack
'''
class min_stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val):
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)
        
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self):
        return self.stack[-1]
    
    def get_min(self):
        return self.min_stack[-1]
    
obj = min_stack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.get_min()
obj.pop()
obj.top()
obj.get_min()
#%%
'''
42 trapping rain water
'''
class solution:
    def trap(self, height):
        max_l = [0]*len(height)
        max_r = [0]*len(height)
        ans = [0]*len(height)
        for i in range(1,len(height)):
            max_l[i]= (max(height[i-1],max_l[i-1]))
            max_r[len(height)-i-1] = max(height[len(height)-i],max_r[len(height)-i])
        for i in range(len(max_l)):
            ans[i] = max(min(max_l[i],max_r[i]) - height[i],0)
        return sum(ans)
height = [0,1,0,2,1,0,1,3,2,1,2,1]
solution = solution()
ans = solution.trap(height)
#%%
'''
567 permutation in string
'''
class solution:
    def check_inclusion(self, s1, s2):
        # take care of special case
        if len(s1) > len(s2):
            return False
        alph = 'abcdefghijklmnopqrstuvwxyz'
        alph_count = {}
        s1_count = {}
        for i in range(len(alph)):
            alph_count[alph[i]] = 0
        s1_count = alph_count.copy()
        s2_count = alph_count.copy()
        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            
        l = 0
        for r in range(len(s1),len(s2)+1):
            for i in range(l,r):
                s2_count[s2[i]] += 1
            if s1_count ==s2_count:
                return True
            else:
                s2_count = alph_count.copy()
                l += 1
        return False
                
            
s1 = 'adc'
s2 = 'dcda'         
solution = solution()
solution.check_inclusion(s1,s2)
            
            
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
