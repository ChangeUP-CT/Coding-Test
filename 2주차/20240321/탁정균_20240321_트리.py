# 6615: 콜라츠 추측
# 특이사항: 다국어(영어)(한국어 번역)
# 알고리즘 분류: 구현/브루트포스 알고리즘/트리/최소 공통 조상

# 0. [반복문] 마지막 줄에 "0 0" 이 입력될 때까지 계속
# 1. 각 테스트 케이스에 두 정수 A, B 입력
# 2. 주어진 수가 홀수이면 3X + 1를 적용하고,  짝수이면 X / 2를 지속적으로 적용
# 3. 같은 숫자가 나오면 A, B에 대하여 각각 몇 번째 원소인지 출력(단, 1이 나오면 수열은 더 이상 진행하지 않음)

def Collatz(n):
    if n % 2 == 1:
        n = 3 * n + 1
    else:
        n //= 2
    return n


def find_meeting_point(A, B):
    # A와 B의 콜라츠 수열에서 같은 수가 나타나는 첫 번째 지점을 찾는 함수
    steps_A, steps_B = {A: 0}, {B: 0}
    seq_A, seq_B = A, B
    step_count_A, step_count_B = 0, 0

    while True:
        if seq_A != 1:
            seq_A = Collatz(seq_A)
            step_count_A += 1
            if seq_A in steps_B:
                # A의 수열이 B의 수열에 이미 나타난 수를 만났을 때
                return A, step_count_A, B, steps_B[seq_A], seq_A
            steps_A[seq_A] = step_count_A

        if seq_B != 1:
            seq_B = Collatz(seq_B)
            step_count_B += 1
            if seq_B in steps_A:
                # B의 수열이 A의 수열에 이미 나타난 수를 만났을 때
                return A, steps_A[seq_B], B, step_count_B, seq_B
            steps_B[seq_B] = step_count_B

        if seq_A == 1 and seq_B == 1:
            # 두 시퀀스가 동시에 1에 도달했을 때
            break

    return A, steps_A[1], B, steps_B[1], 1


while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break

    if A == B:
        A, S_A, B, S_B, C = A, 0, B, 0, A
    else:
        A, S_A, B, S_B, C = find_meeting_point(A, B)

    print(f"{A} needs {S_A} steps, {B} needs {S_B} steps, they meet at {C}")
