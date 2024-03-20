'''
프로그래머스 - 단어 변환
https://school.programmers.co.kr/learn/courses/30/lessons/43163

'''


# bfs
def solution(begin, target, words):
    n = len(begin)
    visited = [False]*len(words)
    queue = deque()
    queue.append((begin,0))
    while queue:
        cur_w, num = queue.popleft()
        if cur_w == target:
            return num
            
        for i in range(len(words)):
            # 방문하지 않은 정점을 방문
            if not visited[i]:
                cnt = 0 
                # 이 문제에서의 포인트 (간선이 될 수 있는 조건 : 한글자만 달라야 함)
                for j in range(n):
                    if cur_w[j] != words[i][j]:
                        cnt += 1
            # 한글자만 다른 경우는 방문
            if cnt == 1 :
                num += 1
                queue.append((words[i],num)) 
                visited[i] = True
                    
    return 0
