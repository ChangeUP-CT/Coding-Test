# 링크: https://www.acmicpc.net/problem/31562
# 31562: 전주 듣고 노래 맞히기
# 알고리즘 분류: 구현/자료 구조/문자열/브루트포스 알고리즘/해시를 사용한 집합과 맵

# 1. 정환이 음을 아는 노래의 개수 N, 맞힐 노래의 개수 M 입력
# 2. [반복문]노래 제목의 길이 T, 노래 제목 S, 음이름 일곱 개 입력
# 3. [반복문] M개의 줄에 걸쳐 첫 세 음의 음이름 세 개가 공백으로 구분되어 입력
# 4. 노래가 하나만 있으면 노래 제목, 두 개 이상이면 "?", 없으면 "!" 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = dict()  # 곡명과 곡명 길이, 음계를 저장할 딕셔너리

for i in range(N):
    input_string = list(input().split())
    T = input_string[0]
    S = input_string[1]
    pitches = input_string[2:]
    table[i] = [S, pitches]

for _ in range(M):
    # 알고 있는 음(known-pitches, kp)
    kp = list(input().split())
    # 첫 세 음이 kp와 동일한 곡의 제목
    matched = []
    for key in table.keys():
        name = table[key][0]
        pitch_list = table[key][1]
        # 첫 세 음이 동일하면 이름 저장
        if kp == pitch_list[:3]:
            matched.append(name)
        # 해당하는 음악이 2개 이상이면 루프 탈출
        if len(matched) >= 2:
            break

    if len(matched) >= 2:
        print("?")
    else:
        if not matched:
            print("!")
        else:
            print(matched[0])
