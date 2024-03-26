'''
주식가격
https://school.programmers.co.kr/learn/courses/30/lessons/42584
'''




from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        c = prices.popleft()
        count = 0 
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1
        answer.append(count)
    return answer
