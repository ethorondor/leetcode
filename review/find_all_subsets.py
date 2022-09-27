'''
find all subsets
'''
class solutions:
    def subsets(self, nums):
        ans = []
        ans.append([])
        for i in nums:
            n = len(ans)
            for j in range(n):
                sub1 = list(ans[j])
                sub1.append(i)
                ans.append(sub1)
        return ans
nums = [1,3]
s = solutions()
s.subsets(nums)