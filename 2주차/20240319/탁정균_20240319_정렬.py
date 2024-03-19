# 링크: https://www.acmicpc.net/problem/1015
# 1015: 수열 정렬
# 특이사항: 스페셜 저지
# 알고리즘 분류: 정렬

# 1. 배열 A의 크기 N 입력(N은 50 이하의 자연수)
# 2. 0번부터 차례대로 배열 A의 원소 입력
# 3. 0부터 N-1까지의 수를 포함하는 수열 P에 대하여 수열 P를 배열 A에 적용
# 3의 보충설명: P를 A에 적용하면 길이가 N인 배열 B가 되고, B[P[i]] = A[i]임.
# 4. A를 오름차순으로 정렬한 것과 같은 또다른 리스트 생성
# 5. 배열 A의 각 원소가 몇 번째로 작은 숫자인지를 정렬_A 리스트에서 확인 후 P에 삽입
# 6. 완성된 배열 P의 각 원소 출력

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A_sorted = sorted(A)
P = []
for i in range(N):
    idx = A_sorted.index(A[i])
    P.append(idx)
    A_sorted[idx] = -1  # 이미 할당한 숫자를 -1로 대체해 재탐색되지 않도록 처리.

print(*P)
