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