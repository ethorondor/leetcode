'''
number of islands
'''
#%%
from collections import deque
class solutions:
    def num_of_islands(self, grid):
        ans = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            directions = [[0,1],[0,-1],[-1,0],[1,0]]
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    _r = row + dr
                    _c = col + dc
                    if (_r) in range(rows) and (_c) in range(cols) and grid[_r][_c]=='1' and (_r,_c) not in visited:
                        visited.add((_r,_c))
                        q.append((_r,_c))
                                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    ans += 1
                    bfs(r,c)
        return ans
    
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
s = solutions()
s.num_of_islands(grid)
# %%
