"""
출처: https://www.acmicpc.net/problem/3665
"""
from collections import deque

for tc in range(int(input())):
    # 팀의 수(n)
    n = int(input())
    # 작년 순위
    rank = list(map(int, input().split()))

    # 위상정렬을 위한 진입차수 리스트 0으로 초기화
    indegree = [0] * (n+1)
    # 위상정렬을 위한 연결리스트
    graph = [[False] * (n+1) for _ in range(n+1)]
    for i in range(n): # 입력받은 순위정보를 바탕으로 자기자신보다 낮은 노드에 대해서 graph 상에서 연결 & 진입차수 업데이트
        now = rank[i]
        for j in range(i+1, n):
            graph[now][rank[j]] = True
            indegree[rank[j]] += 1

    # 상대적인 등수가 바뀐 쌍의 수(m)
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        # 연결리스트에서 순위정보 바꿔주기 (> 진입차수도 같이 수정되어야 함)
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상정렬 수행
    q = deque() # 위상정렬을 수행하기 위한 큐
    for i in range(1, n+1): # 위상정렬의 초기 큐는 진입차수가 0인 노드를 추가
        if indegree[i] == 0:
            q.append(i)
    
    circle = False
    certain = True
    result = []

    for i in range(n):
        if len(q) == 0:
            circle = True
            break
        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        result.append(now)

        # 현재 확인하고 있는 노드와 연결된 간선 끊기
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
    
    if circle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for r in result:
            print(r, end=' ')
        print()





    