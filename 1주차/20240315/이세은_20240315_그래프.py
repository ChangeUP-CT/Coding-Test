"""
문제출처: https://www.acmicpc.net/problem/2887 
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

# 노드의 개수 입력받기
n = int(input())

# 자기자신으로 노드의 값 초기화 하기
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

# 노드의 x, y, z 좌표 입력받기
x = []
y = []
z = []

for i in range(1, n+1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

# x, y, z 각각 오름차순 정렬
x.sort()
y.sort()
z.sort()

# 각 좌표를 기준으로 구한 최소거리들을 edges 리스트에 추가
edges = []
for i in range(n-1):
    edges.append((x[i + 1][0] - x[i][0], x[i + 1][1], x[i][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i + 1][1], y[i][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i + 1][1], z[i][1]))

# 간선을 비용순으로 정렬
edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
