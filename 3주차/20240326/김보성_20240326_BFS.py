'''
수 찾기
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	256712	79581	52812	30.043%
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

예제 입력 1 
5
4 1 5 2 3
5
1 3 7 9 5
예제 출력 1 
1
1
0
0
1
'''

#N - 수개수
N = int(input())
#A- 수 데이터 리스트
#A 리스트정렬
A = list(map(int, input().split()))
A.sort()

#M 탐색할 숫자 개수 저장
#target_list(탐색할 수 데이터 리스트 저장)
M = int(input())
target_list = list(map(int, input().split()))

for i in range(M):
    find = False
    target = target_list[i]
   #이진 탐색
    start = 0
    end = len(A)-1
#   시작 끝 인덱스, 그리고 인덱스로 반복문 만들기
#   while 시작 <= 종료 인덱스:
#       midindex = 시작+종료/2
#       midv = A[midindex]
#       if midv > target:
#           end = midindex-1
#       elif midv < target:
#           start = midindex+1
#       else:
#           find = True
#           break
    while start <= end:
        midindex = int((start+end)/2)
        midv = A[midindex]
        if midv > target:
            end = midindex-1
        elif midv < target:
            start = midindex+1
        else:
            find = True
            break

    if find:
        print(1)
    else:
        print(0)