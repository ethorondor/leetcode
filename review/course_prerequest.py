'''
can finish course prerequisite
'''
#%%
class solutions:
    def can_finish(self, num_course, prerequisites):
        pre_map = {i:[] for i in range(num_course)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            if pre_map[crs] == []:
                return True
            
            visited.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            pre_map[crs] = []
            return True    
        for crs in range(num_course):
            if not dfs(crs):
                return False
        return True
num_course = 5
prerequisites = [[0,1],[0,2],[1,4],[1,3],[3,4],[4,2]]
s = solutions()
s.can_finish(num_course, prerequisites)
# %%
