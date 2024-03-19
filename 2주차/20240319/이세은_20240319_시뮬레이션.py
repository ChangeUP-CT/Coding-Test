"""
출처: https://www.acmicpc.net/problem/16236
"""
from collections import deque

n = int(input()) # 공간의 크기

# 공간정보
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    for j in range(n):
        if array[i][j] == 9:
            shark_x, shark_y = i, j # 초기 상어의 위치

# 초기 상어의 크기
shark_size = 2

# 방향이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

INF = int(1e9)

# 현재위치에서 이동가능한 모든 위치까지의 거리 구하기
def get_distance():
    # 각 좌표까지의 거리는 모두 -1로 초기화
    dist = [[-1] * n for _ in range(n)]
    # 현재위치는 도달가능
    dist[shark_x][shark_y] = 0

    q = deque([(shark_x, shark_y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == -1 and array[nx][ny] <= shark_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist

time = 0 # 엄마상어를 호출하기까지 걸리는 시간
ate = 0
while True:
    dist = get_distance()

    min_dist = INF
    target_x, target_y = 0, 0
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= array[i][j] < shark_size:
                if dist[i][j] < min_dist:
                    min_dist = dist[i][j]
                    target_x, target_y = i, j
    if min_dist >= INF:
        print(time)
        break
    else:
        ate += 1
        time += min_dist
        array[target_x][target_y] = 9 # 상어를 물고기 자리로 이동시킨다
        array[shark_x][shark_y] = 0 # 상어가 있던 자리는 0으로 만들고
        shark_x, shark_y = target_x, target_y

        if ate >= shark_size:
            shark_size += 1
            ate = 0