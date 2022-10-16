'''
rearrange string
'''
#%%
def reorder(s, indices):
    ans = list(s)
    for i in range(len(s)):
        ans[i] = s[indices[i]]
    return ''.join(ans)

s = 'codeleet'
indices = [4,5,6,7,0,1,2,3]
reorder(s, indices)
# %%
