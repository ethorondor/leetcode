'''
course schedule
'''
#%%
class solutions:
    def can_finish(self, num_courses, prerequisites):
        # map each course to prereq list
        pre_map = {i:[] for i in range(num_courses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
            
        # visit set = all courses along the curr DFS path
        visit_set = set()
        def dfs(crs):
            if crs in visit_set:
                return False
            if pre_map[crs] == []:
                return True
            
            visit_set.add(crs)
            for pre in pre_map[crs]:
                
                if dfs(pre) == False:
                    return False
            visit_set.remove(crs)
            pre_map[crs] = []
            return True
        
        for c in range(num_courses):
            if dfs(c) == False:
                return False
        return True
    
num_courses = 3
prerequisites = [[1,0],[0,2]]
s = solutions()
s.can_finish(num_courses, prerequisites)    
# %%
