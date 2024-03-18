# 링크 - https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    mbti = {'R':0, 'T':1, 'C':2, 'F':3, 'J':4, 'M':5, 'A':6, 'N':7}
    alpha = ['R','T','C','F','J','M','A','N']
    result = [0] * 8 # R,T,C,F,J,M,A,N
    for s, c in zip(survey, choices):
        if c > 4:
            result[mbti[s[1]]] += (c-4)
        elif c < 4:
            result[mbti[s[0]]] += (4-c)
        else:
            continue

    for i in range(4):
        a, b = result[2*i], result[2*i+1]
        if a < b:
            answer += alpha[2*i+1]
        elif a > b:
            answer += alpha[2*i]
        else:
            x, y = alpha[2*i], alpha[2*i+1]
            if x < y:
                answer += x
            else:
                answer += y
    return answer