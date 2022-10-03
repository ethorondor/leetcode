'''
robe houses
'''
class solutions:
    def robe_houses(self, nums):
        rob1 = 0
        rob2 = 0
        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
nums = [2,7,9,3,1]
s = solutions()
s.robe_houses(nums)