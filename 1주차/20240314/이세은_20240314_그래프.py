"""
출처: 이것이 코딩테스트다 Q_43 어두운길
문제: https://minimun92.tistory.com/49
"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 집의 수(n), 도로의 수(m)
n, m = map(int, input().split())

# 각 도로에 대한 정보 추가
edges = []
for _ in range(m):
    x, y, z = map(int, input().split())
    # x와 y번 집 사이에 있는 도로의 길이가 z
    edges.append((z, x, y))

# 도로비용을 기준으로 오름차순 정렬
edges.sort()

# 부모 노드 자기 자신으로 초기화
parent = [x for x in range(n)]

# 절약할 수 있는 최대 비용
answer = 0

for edge in edges:
    cost, x, y = edge

    # 사이클이 발생하지 않는다면 신장트리로 추가
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
    else:
        answer += cost

print(answer)