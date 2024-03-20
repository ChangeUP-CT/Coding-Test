#https://school.programmers.co.kr/learn/courses/30/lessons/92335
#
import math

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
        n, mod = divmod(n, k)
        rev_base += str(mod)

    for i in list(map(int, ' '.join(rev_base[::-1].split('0')).split())):
        if is_prime(i):
            answer += 1

    return answer