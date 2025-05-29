#%%
class solutions:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """
        Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.

        Example:
        Input: nums = [2, 7, 11, 15], target = 9
        Output: [0, 1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
        """
        num_to_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index
        return []
nums = [2, 7, 11, 15]
target = 9
sol = solutions()
result = sol.two_sum(nums, target)
# %%
