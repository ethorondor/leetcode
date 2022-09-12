'''
next letter
'''
#%%
def next_letter(letter, key):
    l = 0
    r = len(letter) - 1
    while l <= r:
        m = l + (r-l)//2
        if key < letter[m]:
            r = m -1
        if key > letter[m]:
            l = m + 1
    return letter[l%len(letter)]

letter = ['a','d','e','g','j','k']
key = 'h'
next_letter(letter, key)
# %%
