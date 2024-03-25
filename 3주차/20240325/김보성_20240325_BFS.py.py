'''
미로 탐색
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	192 MB	196314	89481	56869	44.025%

문제
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

예제 입력 1 
4 6
101111
101010
101011
111011
예제 출력 1 
15
예제 입력 2 
4 6
110110
110110
111111
111101
예제 출력 2 
9
예제 입력 3 
2 25
1011101110111011101110111
1110111011101110111011101
예제 출력 3 
38
예제 입력 4 
7 7
1011111
1110001
1000001
1000001
1000001
1000001
1111111
예제 출력 4 
13
'''
'''
방향 정의
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

A초기화 [[0]이 N*M]
방문리스트 = [[False] * M for _ in range(N)]
입력 받기 N, M

자료구조초기화
for y in range (N):
    numbers = list(input())
    for x in range(M):
        A[y][x] = int(numbers[x])

def BFS(i, j):
    queue = deque()
    큐에 시작노드 삽입
    시작노드 방문리스트 True
    큐에 있는게 아무것도 없을때까지 할거임:
        현재 = 큐에서 pop
        ##상하좌우 움직이기
        for k in range(4):
            x = now[0]+dx[k]
            y = now[1]+dy[k]
            if 유효한 좌표: #좌표가 N,M안에 있는지
                A[x][y] != 0 && 방문리스트가 False면
                    방문[x][y] xmfn
                    A[x][y] = A[now[0]][now[1]]+1
                    queue.append((x,y))

BFS(0,0)

print(A[N-1][M-1])
'''

import sys
from collections import deque

input = sys.stdin.readline
#상하좌우 파라미터
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
'''
입력 받기 N, M
A초기화 [[0]이 N*M]
방문리스트 = [[False] * M for _ in range(N)]

'''
A = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]
#print(A)

#자료구조초기화
for y in range (N):
    numbers = list(input())
    for x in range(M):
        A[y][x] = int(numbers[x])

def BFS(i, j):
    queue = deque()
    #큐에 시작노드 삽입
    queue.append((i,j))
    #시작노드 방문리스트 True
    visited[i][j] = True
    #큐에 있는게 아무것도 없을때까지 할거임:
    while queue:
        #현재 = 큐에서 pop
        now = queue.popleft()
    ##상하좌우 움직이기
        for k in range(4):
            x = now[0]+dx[k]
            y = now[1]+dy[k]
            #if 유효한 좌표: #좌표가 N,M안에 있는지
            if x>=0 and y>=0 and x< N and y<M :
        #        A[x][y] != 0 && 방문리스트가 False면
                if A[x][y] != 0 and visited[x][y] == False :
        #            방문[x][y] 트루
                    visited[x][y] = True
                    A[x][y] = A[now[0]][now[1]]+1
                    queue.append((x,y))

BFS(0,0)

print(A[N-1][M-1])