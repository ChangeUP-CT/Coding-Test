"""
5653. [모의 SW 역량테스트] 줄기세포배양
출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRJ8EKe48DFAUo
"""

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for test_case in range(1, 1+T):
    n, m, k = map(int, input().split())
    live = [[0]*(m+2*k+2) for _ in range(n+2*k+2)]
    check = [[0]*(m+2*k+2) for _ in range(n+2*k+2)]
    for i in range(n):
        data = list(map(int, input().split()))
        for j in range(m):
            live[i][j] = data[j]
            if data[j] > 0:
                check[i][j] = -(data[j])

    for _ in range(k):
        l = [[0]*(m+2*k+2) for _ in range(n+2*k+2)]
        for i in range(n+2*k+2):
            for j in range(m+2*k+2):
                if live[i][j] == 0 or live[i][j] == -1:
                    continue
                if check[i][j] < 0:
                    if check[i][j] == -1:
                        check[i][j] = live[i][j]
                    else:
                        check[i][j] += 1
                elif check[i][j] > 0:
                    x, y = i, j
                    for p in range(4):
                        nx = (x+dx[p]) % (n+k*2+2)
                        ny = (y+dy[p]) % (m+k*2+2)
                        if live[nx][ny] == -1 or live[nx][ny] > 0:
                            continue
                        if l[nx][ny] == 0:
                            l[nx][ny] = live[x][y]
                            check[nx][ny] = -live[x][y]
                        elif l[nx][ny] < live[x][y]:
                            l[nx][ny] = live[x][y]
                            check[nx][ny] = -live[x][y]
                    if check[i][j] == 1:
                        live[i][j] = -1
                        check[i][j] = 0
                    else:
                        check[i][j] -= 1

        for i in range(n+2*k+2):
            for j in range(m+2*k+2):
                if l[i][j] > 0 and live[i][j] == 0:
                    live[i][j] = l[i][j]

    cnt = 0
    for i in range(n+2*k+2):
        for j in range(m+2*k+2):
            if check[i][j] != 0:
                cnt += 1
    print(f'#{test_case} {cnt}')