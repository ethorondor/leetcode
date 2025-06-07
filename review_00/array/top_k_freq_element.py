# 347 leetcode top k frequent elements
#%%
class Solution:
    def top_k_freq(self, nums, k):
        import heapq
        hash_set = {}
        for n in nums:
            if n not in hash_set:
                hash_set[n] = 0
            hash_set[n] += 1
        h = []
        for key, values in hash_set.items():
            heapq.heappush(h,[-values, key])
        res = [heapq.heappop(h)[1] for i in range(k)]
        return res
    
nums = [4, 1, -1, 2, -1, 2, 3]
k = 2
sln = Solution()
print(sln.top_k_freq(nums, k))  # Output: [-1, 2]
# %%
