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
