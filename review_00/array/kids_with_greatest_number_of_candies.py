#%%
class solutions:
    def kids_with_greatest_candies(self, candies, extra_candies):
        max_candies = max(candies)
        res = []*len(candies)
        for  n in range(len(candies)):
            if candies[n] + extra_candies >= max_candies:
                res.append(True)
            else:
                res.append(False)
        return res 
candies = [2,3,5,1,3]
extra_candies = 3 
sln = solutions()
sln.kids_with_greatest_candies(candies, extra_candies)
# %%
