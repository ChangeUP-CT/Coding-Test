#https://www.acmicpc.net/problem/1167
'''
문제
트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.

입력
트리가 입력으로 주어진다. 먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고

(2 ≤ V ≤ 100,000)둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다. 정점 번호는 1부터 V까지 매겨져 있다.

먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데, 하나는 정점번호, 다른 하나는 그 정점까지의 거리이다. 

예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다.

각 줄의 마지막에는 -1이 입력으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.

출력
첫째 줄에 트리의 지름을 출력한다.

예제 입력 1 
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1
예제 출력 1 
11
'''
from collections import deque

N= int(input())
A = [[] for _ in range(N+1)]

for _ in range(N):
# A에 그래프 데이터 저장
    Data = list(map(int, input().split())) #[1, 3, 2, -1]
    index = 0 #index = 0
    S =  Data[index] #S = 1
    index += 1 #index = 1
    while True:
        E = Data[index] #1 : E = Data[1] = 3
        if E == -1: 
            break
        V = Data[index+1] #1 : V = 2
        A[S].append((E,V)) #1 : A[1] = (3, 2)
        index += 2 #다음거 보기, 노드, 거리 이렇게 두개를 봐야되므로 인덱스 두개 이동

#거리랑 방문 리스트 초기화/시작노드를 바꾸며 탐색할 것이라 노드가 바뀔 때 새로 초기화를 해주어야함.
distance = [0]*(N+1)
visited = [False]*(N+1)

#BFS 하기
#큐만들기, 큐에 첫번째 노드 넣기, 방문리스트 트루
def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:#큐에 아무것도 없을 때 까지
        now_Node = queue.popleft() #현재노드는 큐에 들어있던것, 그리고 큐에서 pop
        for i in A[now_Node]:#i = 튜플
            if not visited[i[0]]:
                visited[i[0]]= True
                queue.append(i[0])
                distance[i[0]] = distance[now_Node] + i[1] #거리 리스트를 업뎃

BFS(1)
Max = 1

for i in range(2, N+1):
    if distance[Max] < distance[i]:
        Max = i #거리 리스트 값 중에 Max값으로 시작점을 재설정
        #거리가 가장 먼 노드가 Max인거임

distance = [0]*(N+1)
visited = [False]*(N+1)
BFS(Max)

distance.sort()
print(distance[N])
##최대값 출력 -> 정렬후 맨끝값 출력







