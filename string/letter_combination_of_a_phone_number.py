'''
17 letter combinations of a phone number
'''
#%%
digits = '234'

class Solutions:
    def letter_combinations(self, digits):
        dict = {'2':'abc',
                '3':'def',
                '4':'ghi',
                '5':'jkl',
                '6':'mno',
                '7':'pqrs',
                '8':'tuv',
                '9':'wxyz'}
        res = []
        def backtrack(i, curr_str):
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return
            for c in dict[digits[i]]:
                backtrack(i+1, curr_str+c)
        if digits:
            backtrack(0,'')
        return res
sln = Solutions()
sln.letter_combinations(digits)
# %%
