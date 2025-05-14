#%%
class solutions:
    def two_sum(self, nums, target):
        hash_map = {}
        for ind, num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                return [ind, hash_map[diff]]
            hash_map[num] = ind
        return None
nums = [1,3,6,7]
target = 9
s = solutions()
s.two_sum(nums, target)
# %%
