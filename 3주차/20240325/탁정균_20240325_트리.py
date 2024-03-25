# 11725: 트리의 부모 찾기
# 알고리즘 분류: 그래프 이론/그래프 탐색/트리/너비 우선 탐색/깊이 우선 탐색
# 유의사항: Python 3로 풀면 4288ms 걸리는 문제가 Pypy 3 쓰면 292ms로 줄어듭니다.
# 푸실 분들 참고하세요.

# 1. 노드의 개수 N 입력
# 2. N개의 줄에 걸쳐 트리 상에서 연결된 두 노드 입력
# 3. 루트에 해당하는 1번 노드부터 BFS 실시
# 4. 2번 노드부터 순서대로 부모 노드 번호 출력

from collections import deque

N = int(input())
tree = [[] for _ in range(N + 1)]
parent = [-1 for _ in range(N + 1)]
for _ in range(N - 1):
    p, s = map(int, input().split())
    tree[p].append(s)
    tree[s].append(p)


def bfs(graph, start, visited):
    q = deque([start])

    while q:
        p = q.popleft()
        for i in graph[p]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = p


bfs(tree, 1, parent)
for i in parent[2:]:
    print(i)
