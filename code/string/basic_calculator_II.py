'''
s = '2 + 2*3 - 5 +4/5'
'''
#%%
class solutions:
    def calculation(self, s):
        num = 0
        sign = '+'
        stack = []
        s = s + '+'
        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
            elif i in '+-*/':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                elif sign == '/':
                    stack.append(int(stack.pop()/num))
                sign = i
                num = 0
        return sum(stack)  
string = '2+2*3-5+4/4'
solution = solutions()
solution.calculation(string)
# %%
