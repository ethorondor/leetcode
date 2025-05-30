#%%
class solutions:
    def greatest_common_string(self, str1, str2):
        l1, l2 = len(str1), len(str2)
        #define a helper function
        def find_common_string(l):
            if str1%l or str2%l:
                return False
            m1 = l1//l
            m2 = l2//l
            return (str1[:l]*m1 == str1 and str2[:l]*m2 == str2)
        for l in range(min(l1, l2), 0, -1):
            if find_common_string:
                return str1[:l]
        return ''
str1 = 'ABCABC'
str2 = 'ABC'
sln = solutions()
sln.greatest_common_string(str1, str2)
            
# %%
