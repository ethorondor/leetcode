'''
get maximum dishes
'''
#%%
def get_max_dishes(N, D, K):
    dish_eaten = []
    dish_eaten.append(D[0])
    res = 0
    for i in range(1, len(D)):
        if D[i] not in dish_eaten:
            res += 1
            dish_eaten.append(D[i])
        while len(dish_eaten) > K:
            dish_eaten.pop(0)
    return res
N = 6
D = [1,2,3,3,2,1]
K = 1
get_max_dishes(N, D, K)
# %%
