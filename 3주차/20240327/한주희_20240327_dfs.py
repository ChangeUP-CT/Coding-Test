'''
프로그래머스 - 여행경로
https://school.programmers.co.kr/learn/courses/30/lessons/43164

point : defaultdict
- 처음에 defaultdict 아닌 기본 dict 썼다가 keyerror가 났음
- bfs로 모든 문제를 풀려고 했던 것 같다, dfs 문제도 많이 풀어야겠다
'''


def solution(tickets):
    from collections import defaultdict
    
    # 일반 dict 썼더니, keyerror 발생
    graph = defaultdict(list)
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)
    visited = []
    def dfs(a):
        while graph[a]:
            b = graph[a].pop()
            dfs(b)
        visited.append(a)
    dfs('ICN')
    # dfs로 반대로 visited에 추가되기 때문에, 다시 순서 돌려줌    
    return visited[::-1]
