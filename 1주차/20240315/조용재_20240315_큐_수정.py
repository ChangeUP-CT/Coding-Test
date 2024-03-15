# 링크 - https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque
def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)

    sum1, sum2 = sum(q1), sum(q2)
    total = sum1 + sum2
    if sum1 == sum2:
        return 0
    if total % 2 != 0:
        return -1

    count = 0
    limit = len(q1)*3

    while True:
        if sum1 > sum2:
            count+=1
            num = q1.popleft()
            q2.append(num)
            sum1 -= num
            sum2 += num
        elif sum1 < sum2:
            count+=1
            num = q2.popleft()
            q1.append(num)
            sum2 -= num
            sum1 += num

        if count == limit:
            return -1

        # sum1, sum2 = sum(q1), sum(q2)
        if sum1 == sum2:
            return count
        else:
            continue

    return count
