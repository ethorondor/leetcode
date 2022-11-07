'''
basic calculator
s = '2 + 3 - 6'
'''
#%%
class solutions:
    def basic_calculator(self, s):
        num = 0
        sign = '+'
        stack = []
        s = s+'+'
        for n in s:
            if n.isdigit():
                num = num*10 + int(n)
            elif n in '+-*/':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                sign = n
                num = 0
        return sum(stack)
        
s = '2+4-5'
solution = solutions()
solution.basic_calculator(s)
# %%
