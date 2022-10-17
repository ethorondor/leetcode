'''
course schedule II
'''
#%%

class solutions:
    def course_schedule(self, num_course, prerequesites):
        pre_map = {c:[] for c in range(num_course)}
        for crs, pre in prerequesites:
            pre_map[crs].append(pre)
        cycle = set()
        visited = set()
        output = []
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in pre_map[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs) 
            return True   

        for c in range(num_course):
            if dfs(c) == False:
                return []
        return output
    
num_course = 3
prerequesites = [[1,0],[0,2]]
s = solutions()
s.course_schedule(num_course, prerequesites)
# %%
