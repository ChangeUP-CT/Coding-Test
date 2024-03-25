#https://school.programmers.co.kr/learn/courses/30/lessons/92335
import math

#소수 판별 함수
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer=0
    rev_base = ''

    while n > 0:
        # 몫과 나머지
        n, mod = divmod(n, k)
        rev_base += str(mod)

    # 나머지를 반대 순서로 이어붙였으니 슬라이싱으로 순서 반대로 다시 수정
    for i in list(map(int, rev_base[::-1].split('0'))):
        if is_prime(i):
            answer += 1

    return answer