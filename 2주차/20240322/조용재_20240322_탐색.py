# 백준 https://www.acmicpc.net/problem/18352
# 모든 간선의 가중치가 같은 경우에는 BFS를 사용해보자
from collections import deque

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
# 모든 도시에 대한 최단 거리 -1로 초기화
distance = [-1] * (n+1)
distance[x] = 0
q = deque([x])

# BFS 탐색 시작
# 큐에 든게 없을 때까지
while q:
    now = q.popleft()
    # 현재 노드에서 이동할 수 있는 모든 도시 체크
    for next_node in graph[now]:
        # 방문 안한 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 k인 모든 도시 번호
check = False

for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
# k가 없으면
if check == False:
    print(-1)