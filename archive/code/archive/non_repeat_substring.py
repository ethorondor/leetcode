'''
longest substring with distinct characters
'''
class solution:
    def non_repeat_substring(self, str):
        l = 0
        sub_str = []
        sub_str_len = 0
        for r in range(len(str)):

            while str[r] in sub_str:
                sub_str.remove(str[l])
                l += 1
            sub_str.append(str[r])
            sub_str_len = max(len(sub_str),sub_str_len)
        return sub_str_len
str = 'abccde'
solution = solution()
solution.non_repeat_substring(str)
#