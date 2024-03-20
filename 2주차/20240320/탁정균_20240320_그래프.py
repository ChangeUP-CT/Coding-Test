# 링크: https://www.acmicpc.net/problem/16173
# 16173: 점프왕 쩰리 (Small)
# 특이사항: 시간 제한 1초 (추가 시간 없음)
# 알고리즘 분류: 구현/그래프 이론/브루트포스 알고리즘/그래프 탐색/너비 우선 탐색/깊이 우선 탐색

# 1. 게임 구역의 크기 N (2 ≤ N ≤ 3) 입력
# 2. [반복문] 두 번째 줄부터 마지막 줄까지 게임판의 구역(맵) 입력
# 2의 추가설명: 게임판의 승리 지점(오른쪽 맨 아래 칸)에는 -1이 쓰여있고, 나머지 칸에는 0 이상 100 이하의 정수가 쓰여짐.
# 3. 왼쪽 맨 윗 칸을 시작점으로 지정, dfs를 실행(현재 밟고 있는 칸의 숫자만큼 이동해야 함)
# 4. 실행 결과 도착점의 인덱스가 True 처리되어 있다면 도달했음을 의미
# 5. 끝점에 도달할 수 있으면 "HaruHaru", 도달할 수 없으면 "Hing" 출력

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]


def dfs(x, y):
    visited[x][y] = True
    dx = [graph[x][y], 0]
    dy = [0, graph[x][y]]

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            dfs(nx, ny)


dfs(0, 0)

if visited[N - 1][N - 1]:
    print("HaruHaru")
else:
    print("Hing")
