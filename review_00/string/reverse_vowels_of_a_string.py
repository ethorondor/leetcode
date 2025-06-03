#%%
class solutions:
    def reverse_vowels(self, s):
        string = [i for i in s]
        vowels = ['a','e','i','o','u']
        l, r = 0, len(string) - 1
        while l < r:
            if string[l].lower() in vowels and string[r].lower() in vowels:
                string[l], string[r] = string[r], string[l]
                l += 1
                r -= 1
            elif string[l].lower() in vowels and string[r].lower() not in vowels:
                r -= 1
            elif string[l].lower() not in vowels and string[r].lower() in vowels:
                l += 1
            else:
                l += 1
                r -= 1
        return ''.join(string)
s = "IceCreAm"
sln = solutions()
sln.reverse_vowels(s)
# %%
