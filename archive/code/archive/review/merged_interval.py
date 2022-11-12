'''
merged interval
'''
#%%
class solutions:
    def merged_interval(self, intervals):
        intervals.sort(key=lambda x:x[0])
        merged_intervals = []
        merged_intervals.append(intervals[0])
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] < intervals[i+1][0]:
                i += 1
                
            elif intervals[i][1] <= intervals[i+1][1]:
                _tmp = [intervals[i][0],intervals[i+1][1]]
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i,_tmp)
        return intervals
        
        
intervals = [[1,3],[2,4],[5,7]]
s = solutions()
s.merged_interval(intervals)
# %%
