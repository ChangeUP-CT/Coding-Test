"""
5653. [모의 SW 역량테스트] 줄기세포배양
출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRJ8EKe48DFAUo
"""
import sys
sys.stdin = open('input.txt', 'r')
class cell:
    def __init__(self, x, y, time):
        self.hp=x # 비활성화에서 활성화까지 남은시간 혹은 활성화에서 죽을 때까지 시간
        self.ahp=x # 활성화하는데 걸리는 시간
        self.status=y # 1 비활성, 2 활성, 3 죽음, 0 없음
        self.time=time # 생성된 시간

def spread(x, y, w, t):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if map1[nx][ny].status == 0:
            map1[nx][ny].status = 1
            map1[nx][ny].hp = w
            map1[nx][ny].ahp = w
            map1[nx][ny].time = t
        elif map1[nx][ny].status == 1 and map1[nx][ny].time == t:
            if w > map1[nx][ny].hp:
                map1[nx][ny].hp = w
                map1[nx][ny].ahp = w


T = int(input())
for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    current_time = 0
    map1 = [[cell(0, 0, 0) for _ in range(m+k)] for _ in range(n+k)]
    map2 = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if map2[i][j] != 0:
                map1[i + k // 2][j + k // 2].status = 1
                map1[i + k // 2][j + k // 2].hp = map2[i][j]
                map1[i + k // 2][j + k // 2].ahp = map2[i][j]

    sero = len(map1)
    garo = len(map1[0])
    while current_time < k:
        current_time += 1
        for x in range(sero):
            for y in range(garo):
                if map1[x][y].status == 1 and map1[x][y].time < current_time:
                    map1[x][y].hp -= 1
                    if map1[x][y].hp == 0:
                        map1[x][y].status = 2
                        map1[x][y].hp = map1[x][y].ahp
                        continue
                elif map1[x][y].status == 2:
                    map1[x][y].hp -= 1
                    if map1[x][y].hp == map1[x][y].ahp-1:
                        spread(x, y, map1[x][y].ahp, current_time)
                    if map1[x][y].hp == 0:
                        map1[x][y].status = 3
    answer = 0
    for i in range(sero):
        for j in range(garo):
            if map1[i][j].status == 1 or map1[i][j].status == 2:
                answer += 1

    print(f"#{tc} {answer}")
