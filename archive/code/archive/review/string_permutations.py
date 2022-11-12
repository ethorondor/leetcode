'''
permutation of strings
'''
#%%
class solutions:
    def string_permutations(self, str):
        permutations = []
        permutations.append(str)
        for i in range(len(str)):
            if str[i].isalpha():
                n = len(permutations)
                for _ in range(n):
                    char = list(permutations[_])
                    char[i]=char[i].swapcase()
                    permutations.append(''.join(char))
        return permutations
str = 'ad52'
s = solutions()
s.string_permutations(str)        
# %%
