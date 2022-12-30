'''
128. longest consecutive sequence
Given an unsorted array of integers, return the length of the longest consecutive elements sequence.
'''
#%%
from typing import List
class solutions:
    def longest_consecutive_sequence(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for n in nums:
            # check if its the start of a sequence
            if (n-1) not in num_set:
                length = 0
                while (n+length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest
nums = [100, 4, 200, 2, 1, 3]
sln = solutions()
sln.longest_consecutive_sequence(nums)
# %%
