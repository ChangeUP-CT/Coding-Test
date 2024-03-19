'''
https://leetcode.com/problems/number-of-islands/submissions/1207049894/ 
Number of Islands 구하기
'''

class Solution(object):
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        # 방문 표시할 2차원 배열(grid와 동일한 사이즈)
        visited = [[False]*n for i in range(m)]
        num = 0 
        def bfs(x,y):
            queue = deque()
            queue.append((x,y))
            while queue:
                visited[x][y] = True
                cur_x,cur_y = queue.popleft()
                dx = [-1,1,0,0]
                dy = [0,0,-1,1]
                for i in range(4):
                    next_x = cur_x + dx[i]
                    next_y = cur_y + dy[i]
                    if next_x>=0 and next_x<m and next_y >=0 and next_y<n:
                        if grid[next_x][next_y]=='1'and not visited[next_x][next_y]:
                            visited[next_x][next_y] = True
                            queue.append((next_x,next_y))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i,j)               
                    num += 1
        return num
