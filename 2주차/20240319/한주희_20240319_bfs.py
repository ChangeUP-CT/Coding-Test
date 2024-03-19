'''
1091. Shortest Path in Binary Matrix
https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

'''

# 최단거리 -> bfs
def shortestPath(grid):
    shortest_path = -1
    row = len(grid)
    col = len(grid[0])
    
    # 출발지가 0,0이 아닌 경우, 목적지가 오른쪽 맨아래가 아닌 경우
    if grid[0][0] != 0 or grid[row-1][col-1] != 0:
        return shortest_path
    # x, y, 길이 정보
    queue = deque()
    queue.append((0,0,1))
    # 생각할 거리 -> visited말고, grid 자체 값을 바꿔서 방문 체크 할 수도 있음 (But, 디버깅할 때 혼란이 있을 수도 있음)
    visited = [[False]*col for _ in range(row)]
    visited[0][0] = True
    # 8개의 방향에 접근
    delta = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    while queue:
        cur_x,cur_y,cur_len = queue.popleft()
        # 목적지에 도착했을 때(좌표가 오른쪽 맨 아래일때) cur_len을 shortest_path 에 저장하고 break
        if cur_x == row-1 and cur_y == col-1:
            shortest_path = cur_len
            break
        # 연결되어 있는 vertex 확인
        for dr,dc in delta:
            next_x = cur_x + dr
            next_y = cur_y + dc
            if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:
                if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                    queue.append((next_x,next_y,cur_len+1))
                    visited[next_x][next_y] = True
    
    return shortest_path
