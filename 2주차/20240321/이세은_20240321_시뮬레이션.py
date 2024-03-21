"""
출처: https://www.acmicpc.net/problem/19237
"""

n, m, k = map(int, input().split())

# 격자
array = [list(map(int, input().split())) for _ in range(n)]

# 각 상어의 방향 (1 위, 2 아래, 3 왼쪽, 4 오른쪽)
directions = list(map(int, input().split()))

# 각 상어의 방향 우선순위
priorities = [[] for _ in range(m)]
for i in range(m):
    for _ in range(4):
        priorities[i].append(list(map(int, input().split())))

### 냄새정보 업데이트
smell = [[[0, 0]] * n for _ in range(n)] # (냄새번호, 남은시간)
def update_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0: # 냄새가 존재하는 경우 시간을 1만큼 감소시키기
                smell[i][j][1] -= 1
            if array[i][j] != 0: # 격자에 상어가 있는 위치에 냄새정보 업데이트
                smell[i][j] = [array[i][j], k]


### 상어의 이동 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def move():
    # 이동결과를 담기 위한 임시결과 테이블 초기화
    new_array = [[0] * n for _ in range(n)]
    # 각 위치를 하나씩 확인하면서
    for x in range(n):
        for y in range(n):
            if array[x][y] != 0: # 상어가 존재하는 경우
                # 현재 상어가 바라보고있는 방향
                direction = directions[array[x][y]-1]
                # 현재 방향에서 우선순위에 따라서 방향체크하면서 냄새가 존재하지 않는 곳 찾기
                found = False # 냄새가 존재하지 않는 곳의 존재 여부
                for index in range(4):
                    nx = x + dx[priorities[array[x][y]-1][direction-1][index]-1]
                    ny = y + dy[priorities[array[x][y]-1][direction-1][index]-1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][1] == 0: # 냄새가 존재하지 않는 곳이라면
                            directions[array[x][y]-1] = priorities[array[x][y]-1][direction-1][index] # 현재 상어의 방향 업데이트
                            # 상어 이동시키기 (단, 이전에 미리 해당 위치로 이동한 상어가 있는 경우 값이 작은 상어로 업데이트)
                            if new_array[nx][ny] == 0:
                                new_array[nx][ny] = array[x][y]
                            else:
                                new_array[nx][ny] = min(new_array[nx][ny], array[x][y])
                            found = True
                            break
                if found:
                    continue

                # 냄새가 존재하지 않는 곳이 없으면 현재 방향을 기준으로 우선순위대로 4방향 살펴서 자신의 냄새가 있는 곳으로 이동
                for index in range(4):
                    nx = x + dx[priorities[array[x][y]-1][direction-1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][0] == array[x][y]: #자신의 냄새가 있는 곳이면
                            # 상어이동시키기
                            directions[array[x][y]-1] = priorities[array[x][y]-1][direction-1][index]
                            new_array[nx][ny] = array[x][y]
                            break
    return new_array

time = 0
while True:
    update_smell()
    new_array = move()
    array = new_array
    time += 1

    # 1번 상어만 남았는지 체크
    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False

    if check:
        print(time)
        break

    if time >= 1000:
        print(-1)
        break