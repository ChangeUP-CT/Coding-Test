# 링크 - https://www.acmicpc.net/problem/1260
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(graph, V, visited):
    '''
    :param graph: 그래프 맵
    :param V: 시작 인덱스
    :param visited: 방문 기록
    재귀를 통해 방문 안했으면 계속 탐색
    '''
    print(V , end=' ')
    visited[V] = 1
    for node in graph[V]:
        if not visited[node]:
            dfs(graph, node, visited)
def bfs(graph, V, visited):
    '''
    :param graph: 그래프 맵
    :param V: 시작 노드
    :param visited: 방문 기록
    방문하지 않은 노드라면 큐에 넣고 큐가 빌떄까지 반복
    '''
    que = deque()
    que.append(V)
    visited[V] = 1

    while(que):
        v = que.popleft()
        print(v , end=' ')
        for node in graph[v]:
            if not visited[node]:
                visited[node] = 1
                que.append(node)


visited = [0] * (N+1)
dfs(graph, V, visited)
print()
visited = [0] * (N+1)
bfs(graph, V, visited)