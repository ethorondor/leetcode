#%%
'''
longest substring with same letters after replacement
'''
class solution:
    def length_of_longest_substring(self, str1,k):
        l = 0
        max_length = 0
        str_dict = {}
        for r in range(len(str1)):
            if str1[r] not in str_dict:
                str_dict[str1[r]] = 1
            else:
                str_dict[str1[r]]+= 1
            while sum(str_dict.values()) - max(str_dict.values()) >2:
                str_dict[str1[l]] -= 1
                l += 1
                
            max_length = max(max_length, sum(str_dict.values()))
        return max_length
str1 = 'abccde'
solution = solution()
solution.length_of_longest_substring(str1,2)
                
