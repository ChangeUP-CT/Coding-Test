'''
프로그래머스 - 정수 삼각형
https://school.programmers.co.kr/learn/courses/30/lessons/43105
'''



def solution(triangle):
    n = len(triangle) 
    # 결과를 담아줄 DP Table
    dp = [[0]* (i+1) for i in range(n)]
    dp[0][0] = triangle[0][0]
    for i in range(1,n):
        for j in range(i+1):
            # 왼쪽 끝에 있는 경우
            if j == 0: 
                dp[i][j] = triangle[i][j] + dp[i-1][j] 
            # 오른쪽 끝에 있는 경우
            elif i == j:
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
            # 왼, 오에서 온 경우에 대해 max값을 반환해서 dp에 저장
            else:
                dp[i][j] = max(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])
    # 가장 아래 줄 max값
    return max(dp[-1])
