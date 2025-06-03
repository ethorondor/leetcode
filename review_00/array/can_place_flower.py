#%%
from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        can_place = 1
        res = 0
        for i in range(len(flowerbed)):
            if i < len(flowerbed) - 1:
                if flowerbed[i] == 0:
                    if can_place == -1:
                        can_place = -1*can_place
                    elif can_place == 1:
                        if flowerbed[i+1] == 0:
                            res += 1
                            can_place = -1*can_place
                elif flowerbed[i] == 1:
                    can_place = -1
            else:
                if can_place == 1:
                    if flowerbed[i] == 0:
                        res += 1
        return n<=res
flowerbed = [1,0,0,0,1]
n = 2
sln = Solution()
sln.canPlaceFlowers(flowerbed, n)
# %%
