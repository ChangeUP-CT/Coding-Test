# 링크: https://www.acmicpc.net/problem/19592
# 19592: 장난감 경주
# 특이사항: 다국어(영어)(한국어 번역)
# 알고리즘: 수학/브루트포스 알고리즘/이분 탐색 (← 백준에선 이진 탐색을 이분 탐색이라고 부르네요)

# 제한사항
# 1 ≤ T ≤ 10
# 2 ≤ N ≤ 1,000
# 1 ≤ Y ≤ X ≤ 1,000,000
# 1 ≤ V[i] ≤ 1,000,000

# 1. 테스트 케이스의 개수 T 입력
# 2. [반복문]
# 2-1. 각 테스트 케이스의 첫 줄에 참가자의 수 N, 트랙 길이 X, 부스터 속도 한계치 Y 입력
# 2-2. N개의 정수 입력 - 각 장난감 자동차의 속도 V[i]를 의미
# 2-3. V[1]부터 V[N-1]까지는 주어진 속도대로 트랙을 완주하는 시간 계산
# 2-4. 주어진 속도 중 최고 속도보다 큰 속도부터 시작해 Y가 될 때까지 자신의 속도를 바꿔가면서 계산
# 2-5-1. 단독 우승이 가능한 속도가 계산되면 해당 정수 Z를 출력
# 2-5-2. 부스터 없이도 단독 우승이 가능하다면 0을 출력
# 2-5-3. 부스터를 최대로 사용하고도 단독 우승이 불가능하다면 -1을 출력

import sys
input = sys.stdin.readline


# 부스터를 켰을 때 트랙을 도는 시간
def booster(X, v, v_b):
    '''
    Variables
    ========================================
    X: 트랙 길이
    v: 입력받은 나의 속도(아래의 v_N에 해당)
    v_b: 부스터 속도(최대값은 문제에서 주어진 Y)
    '''
    d = X - v_b
    return d / v + 1


T = int(input())
for _ in range(T):
    N, X, Y = map(int, input().split())
    velocities = list(map(int, input().split()))
    v_N = velocities[-1]  # 나의 속도
    max_v = max(velocities)  # 입력받은 속도들 중 최고 속도

    if v_N == max_v:
        print(0)
        continue

    else:
        times = [X / v for v in velocities[:-1]]
        t_N = min(times)
        low, high = 0, Y

        while low <= high:
            mid = (low + high) // 2
            boost = booster(X, v_N, mid)
            if boost >= t_N:
                low = mid + 1
            else:
                high = mid - 1

        if low > Y:
            print(-1)
        else:
            print(low)
