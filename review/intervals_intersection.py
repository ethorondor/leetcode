'''
intervals intersection
'''
#%%
class solutions:
    def intervals_intersection(self, intervals_1, intervals_2):
        ans = []
        i = 0
        j = 0
        while i < len(intervals_1) and j < len(intervals_2):
            if intervals_2[j][0] > intervals_1[i][1]:
                i += 1
            elif intervals_2[j][1] < intervals_1[i][0]:
                j += 1
            else:
                left = max(intervals_1[i][0],intervals_2[j][0])
                right = min(intervals_1[i][1],intervals_2[j][1])
                ans.append([left,right]) 
                i+=1
                j+=1
        return ans
    
arr1 = [[1,3],[5,6],[7,9]]
arr2 = [[2,3],[5,7]]
s = solutions()
s.intervals_intersection(arr1,arr2)
# %%
