'''
basic calculator
input: s = "(23+(4+5+2)-3)+(6+8)"
'''
#%%
class solution:
    def calculation(self, s):
        _num = 0
        _sum = 0
        sign = 1
        stack = []
        
        for char in s:
            
            if char.isdigit():
                _num = _num*10 + int(char)
            elif char in ['+','-']:
                _sum += sign * _num
                if char == '+':
                    sign = 1
                else:
                    sign = -1
                _num = 0
            elif char == '(':
                stack.append(_sum)
                stack.append(sign)
                sign = 1
                _sum = 0
            elif char == ')':
                _sum += sign*_num
                _sum *= stack.pop()
                _sum += stack.pop()
                _num = 0
        return _sum + sign*_num
#s = "(23+(4+5+2)-3)+(6+8)"
s = '2+3+9-29'
solution = solution()
solution.calculation(s)
# %%
