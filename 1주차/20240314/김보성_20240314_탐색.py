"""
출처: Do it! 알고리즘 코딩 테스트 파이썬편
24번 신기한 소수찾기

백준 2023번

[문제]
수빈이가 세상에서 가장 좋아하는 것은 소수이고, 취미는 소수를 가지고 노는 것이다. 요즘 수빈이가 가장 관심있어 하는 소수는 7331이다.

7331은 소수인데, 신기하게도 733도 소수이고, 73도 소수이고, 7도 소수이다. 즉, 왼쪽부터 1자리, 2자리, 3자리, 4자리 수 모두 소수이다! 수빈이는 이런 숫자를 신기한 소수라고 이름 붙였다.

수빈이는 N자리의 숫자 중에서 어떤 수들이 신기한 소수인지 궁금해졌다. N이 주어졌을 때, 수빈이를 위해 N자리 신기한 소수를 모두 찾아보자.

[입력 조건]

첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다.

[출력 조건]

N자리 수 중에서 신기한 소수를 오름차순으로 정렬해서 한 줄에 하나씩 출력한다.

<입력 예시 1>
4

<출력 예시 1>
2333
2339
2393
2399
2939
3119
3137
3733
3739
3793
3797
5939
7193
7331
7333
7393
"""

##재귀함수를 이용해 DFS풀기
import sys
sys.setrecursionlimit(10000) ##재귀함수로 구현하데에는 깊이 제한을 두어야함.
input = sys.stdin.readline


#N 자릿수 입력받기
N = int(input())


"""
isPrime함수(num):
    for i in range(2, int(num/2 + 1)):
        if num % i == 0:
            return False
    return True

DFS 함수:
if 자릿수(DFS의 파라미터 길이) == N:
    현재수 출력
else :
    for i in range(1,10):
        if i 짝수:
            continue
        if isPrime(number*10+i):
            DFS(number*10+i) -------------->홀수이고 소수면 더 깊게 탐색

 
"""
def isPrime(num):
    for i in range(2, int(num/2 + 1)):
        if num % i == 0:
            return False
    return True

def DFS(number):
    if len(str(number)) == N:
        print(number)
    else:
        for i in range(1,10):
            if i % 2 == 0:
                continue
            if isPrime(number*10+i):
                DFS(number*10+i) ##-------------->홀수이고 소수면 더 깊게 탐색


DFS(2)
DFS(3)
DFS(5)
DFS(7)