'''
문제 : 프로그래머스 베스트 앨범
https://school.programmers.co.kr/learn/courses/30/lessons/42579
'''

def solution(genres, plays):
    answer = []
    genres_plays = {}
    num_plays = {}
    '''
    dict 두개를 생성
    1) 장르별 총 재생수 dict (총 재생수에 따른 정렬 위함)
    2) 장르별 재생수 dict (장르 내에서 재생수로 정렬 위함 + 고유번호 출력해야하기 때문에 고유번호도 저장)
    '''
    for i in range(len(genres)):
        n = 0
        if genres[i] in genres_plays:
            genres_plays[genres[i]] += plays[i]
        else:
            n += plays[i]
            genres_plays[genres[i]] = n
        if genres[i] in num_plays:
            num_plays[genres[i]].append([plays[i],i])
        else:
            num_plays[genres[i]] = [[plays[i],i]]
    # 총 플레이 수가 많은 순서대로 장르 정렬
    genres_rank = sorted(genres_plays, key = genres_plays.get, reverse=True)
    for x in genres_rank:
        play_rank = sorted(num_plays[x], key=lambda x: (-x[0], x[1]))
        if len(play_rank) == 1:
            answer.append(play_rank[0][1])
        else:
            answer.append(play_rank[0][1])
            answer.append(play_rank[1][1])
    return answer



'''
백준 1743번 음식물 피하기 
https://www.acmicpc.net/problem/1743

'''

from collections import deque
N, M, K = map(int, input().split())
grid = [[0]*M for _ in range(N)]
# 음식물 위치를 2차원 배열로 표시하자
for i in range(K):
    r, c = map(int,input().split())
    grid[r-1][c-1] = 1

visited = [[False]*M for _ in range(N)]
def bfs(x,y):
    cnt = 1
    queue = deque()
    queue.append((x,y))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited[x][y] = True
    
    while queue:
        cur_x,cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if next_x>=0 and next_x < N and next_y >= 0 and next_y < M:
                if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x,next_y))
                    cnt += 1
    return cnt
num=0
# bfs할때마다 bfs 수행한 숫자를 저장하고, 최댓값을 출력
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1 and not visited[i][j]:
            cur=bfs(i,j)                        
            if cur>num:
                num=cur
                         
print(num)    
            


