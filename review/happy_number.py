'''
happy number
'''
#%%
class solutions:
    def happy_number(self, nums):
        slow = nums
        fast = sum_square_of_digit(nums)
        while fast != 1 and fast != slow:
            slow = sum_square_of_digit(slow)
            fast = sum_square_of_digit(sum_square_of_digit(fast))
        if fast == 1:
            return True
        else:
            return False
    
def sum_square_of_digit(nums):
    ans = 0
    while nums > 0:
        ans += (nums%10)**2
        nums = nums//10
    return ans
s = solutions()
s.happy_number(23)
# %%
