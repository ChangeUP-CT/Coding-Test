# 링크: https://www.acmicpc.net/problem/1972
# 1972: 놀라운 문자열
# 특이사항: 다국어(영어)(원문)
# 알고리즘 분류: 구현/자료 구조/문자열/해시를 사용한 집합과 맵

# 0. [반복문] '*'이 입력되면 프로그램 종료
# 1. 알파벳 대문자로만 구성된 문자열 입력
# 2. [반복문] 0부터 N-2까지 D를 바꿔가며 진행
# 2-1. 집합을 정의 후, D-쌍을 집합에 add
# 2-2. 모든 삽입이 끝난 후, 집합 내의 원소의 개수가 문자열의 길이 - D 와 다를 경우 False 반환.
# 2-3. 모든 D에 대하여 D-유일하면 True 반환.
# 3. True, False에 따라 정해진 양식에 맞춰 정답 출력.


def surprising(string, n):
    for j in range(1, n - 1):
        pairs = set()
        for i in range(n - j):
            pairs.add(''.join([string[i], string[i + j]]))
        if len(pairs) != N - j:
            return False
    return True


while True:
    string = input()
    if string == '*':
        break
    N = len(string)
    if surprising(string, N):
        print(f"{string} is surprising.")
    else:
        print(f"{string} is NOT surprising.")
