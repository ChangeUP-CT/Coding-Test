# 링크: https://www.acmicpc.net/problem/1012
# 1012: 유기농 배추
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색/깊이 우선 탐색

# 1. 테스트 케이스의 개수 T 입력
# 2. [반복문]
# 2-1. 첫째 줄에 배추밭의 가로 길이 M, 세로 길이 N, 배추 위치의 개수 K 입력
# 2-2. 모든 원소가 0인 M x N 그래프 생성
# 2-3. K줄에 걸쳐 배추의 위치 X, Y 입력(중복 없음)
# 2-4. 그래프 상에서 해당 위치의 원소를 1로 변경
# 2-5. DFS를 실시하면서 배추가 심어져 있는 곳에 흰지렁이개수 추가 후 방문 처리(0으로 변경)
# 2-6. 배추흰지렁이의 마릿수 출력

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().rstrip().split())
    graph = [[0] * M for i in range(N)]
    for i in range(K):
        x, y = map(int, input().rstrip().split())
        graph[y][x] = 1

    larva = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                larva += 1

    print(larva)
