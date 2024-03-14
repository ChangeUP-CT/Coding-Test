# 링크 - https://www.acmicpc.net/problem/2606
# 2606: 바이러스
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색/깊이 우선 탐색

# 1. 컴퓨터의 수 입력
# 2. 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수 입력
# 3. 2에서 입력받은 수만큼 한 줄에 한 쌍씩 직접 연결된 컴퓨터의 번호 쌍 입력
# 4. 1번 컴퓨터부터 시작해 DFS를 수행해 순회(탐색에 성공하면 해당 번호의 컴퓨터는 감염 처리)
# 5. 최종적으로 감염된 컴퓨터의 수 출력 (단, 1번 컴퓨터는 개수에서 제외)

N = int(input())
p = int(input())
graph = dict()
for _ in range(p):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = [v]
    else:
        graph[u].append(v)
    # v에서 u로 가는 양방향 연결을 고려해야 함(이 문제는 간선의 방향성이 없기 때문)
    if v not in graph:
        graph[v] = [u]
    else:
        graph[v].append(u)

infected = set()


def dfs(node, visited):
    visited.add(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(neighbor, visited)


dfs(1, infected)

print(len(infected) - 1)  # 1번 컴퓨터는 개수에서 제외
