'''
basic calculator
input: s = "(1+(4+5+2)-3)+(6+8)"
'''
class solution:
    def calculation(self, s):
        cur = res = 0
        sign = 1
        stack = []
        
        for char in s:
            if char.isdigit():
                cur = cur*10 + int(char)
            elif char in ['+','-']:
                res += sign * cur
                sign = 1 if char == '+' else -1
                cur = 0
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif char == ')':
                res += sign*cur
                res *= stack.pop()
                res += stack.pop()
                cur = 0
        return res + sign*cur
s = "(1+(4+5+2)-3)+(6+8)"
solution = solution()
solution.calculation(s)