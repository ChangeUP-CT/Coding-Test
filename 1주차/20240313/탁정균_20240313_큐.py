# 링크 - https://www.acmicpc.net/problem/1021
# 1021: 회전하는 큐
# 유의사항: 큐를 왼쪽으로 한 칸 이동시키는 연산을 2번 연산, 오른쪽으로 한 칸 이동시키는 연산을 3번 연산으로 칭합니다.
# 알고리즘 분류: 자료 구조/덱

# 1. 큐의 크기 N과 뽑아내려고 하는 수의 개수 M 입력
# 2. 뽑아낼 수의 위치를 순서대로 입력
# 3. 1부터 N까지의 자연수를 담은 큐 생성
# 4. [반복문] M개의 수를 뽑을 때까지 반복
# 4-1. 다음으로 뽑을 수가 큐 맨 앞이면 바로 추출
# 4-2. 큐의 중앙보다 앞쪽에 있으면 그 횟수만큼 2번 연산 수행 후 추출
# 4-3. 큐의 중앙보다 뒤쪽에 있으면 그 횟수만큼 3번 연산 수행 후 추출
# 5. 2번과 3번 연산을 수행한 횟수 출력

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
idx_list = list(map(int, input().split()))
q = deque(range(1, N + 1))

cnt = 0
for i in idx_list:
    idx = list(q).index(i)
    if idx <= len(q) // 2:  # 4-2
        while i != q[0]:
            popped = q.popleft()
            q.append(popped)
            cnt += 1
    elif idx > len(q) // 2:  # 4-3
        while i != q[0]:
            popped = q.pop()
            q.appendleft(popped)
            cnt += 1
    q.popleft()

print(cnt)
