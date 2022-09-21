'''
fruits into baskets
'''
#%%
class solutions:
    def fruits_baskets(self, fruit):
        l = 0
        ans = 0
        basket = {}
        for r in range(len(fruit)):
            if fruit[r] not in basket:
                basket[fruit[r]] = 0
            basket[fruit[r]] += 1
            while len(basket) > 2:
                basket[fruit[l]] -= 1
                if basket[fruit[l]] == 0:
                    del basket[fruit[l]]
                l += 1
            ans = max(sum(basket.values()), ans)
        return ans
fruit = ['A','B','C','A','C']
s = solutions()
s.fruits_baskets(fruit)
# %%
