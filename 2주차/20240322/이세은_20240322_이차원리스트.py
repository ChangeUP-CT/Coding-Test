"""
1209. [S/W 문제해결 기본] 2일차 - Sum
출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE
"""

import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc = int(input())

    answer = 0
    array = []
    col_sum = [0] * 100
    diagnal_sum = [0] * 2

    for i in range(100):
        row = list(map(int, input().split()))
        row_sum = sum(row)
        answer = max(answer, row_sum)
        array.append(row)

        for j in range(100):
            col_sum[j] += row[j]
            if i == j:
                diagnal_sum[0] += row[j]
            elif 100 - i - 1 == j:
                diagnal_sum[1] += row[j]

    answer = max(answer, max(col_sum), max(diagnal_sum))
    print(f"#{tc} {answer}")