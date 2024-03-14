# 링크 - https://www.acmicpc.net/problem/1012

import sys
sys.setrecursionlimit(10**6)

T = int(input())


def dfs(ii, jj):
    # 상하좌우 이동을 위한 배열
    di = [1, -1, 0, 0]
    dj = [0, 0, -1, 1]

    # 상하좌우 돌면서 DFS 하기
    for idx in range(4):
        move_i = ii + di[idx]
        move_j = jj + dj[idx]

        if (0 <= move_i < n) and (0 <= move_j < m):
            if graph[move_i][move_j] == 1:
                graph[move_i][move_j] = 0
                dfs(move_i, move_j)


for _ in range(T):
    n, m, k = map(int, input().split())
    graph = [[0] * m for q in range(n)]
    cnt = 0

    for z in range(k):
        i, j = map(int, input().split())
        graph[i][j] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)