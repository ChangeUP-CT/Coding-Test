"""
출처: https://www.acmicpc.net/problem/19236
"""

import copy
# import sys
# sys.stdin = open('input.txt', 'r')

# 초기 배열정보를 입력받음
array = [[] for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        array[i].append([data[2*j], data[2*j+1]-1])

# 방향정보x
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def find_fish_data(array, fish_num): # 물고기의 위치를 찾는 함수 (물고기가 존재하지 않은 경우 None 반환)
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == fish_num:
                return i, j, array[i][j][1]
    return None

# 1번부터 16번까지 차례대로 물고기를 이동시키는 함ㅁ수
def move_fish(array, shark_x, shark_y):
    for fish_num in range(1, 17):
        fish_data = find_fish_data(array, fish_num)
        if fish_data == None:
            continue
        fish_x, fish_y, fish_direction = fish_data
        for i in range(8): # 최대 8번 회전가능하므로
            # 현재 물고기의 위치에서 해당 방향으로 이동한 다음 위치 고려
            fish_nx = fish_x + dx[fish_direction]
            fish_ny = fish_y + dy[fish_direction]
            # 다음위치가 격자 안에 있으면서 상어가 위치한 곳이 아니라면
            if (0 <= fish_nx < 4 and 0 <= fish_ny < 4) and not(fish_nx == shark_x and fish_ny == shark_y):
                array[fish_x][fish_y][1] = fish_direction
                array[fish_x][fish_y], array[fish_nx][fish_ny] = array[fish_nx][fish_ny], array[fish_x][fish_y],
                break
            # 격자안에 없거나 상어가 위치한 곳이라면 회전
            fish_direction = (fish_direction + 1) % 8

# 현재의 위치에서 상어가 이동가능한 위치 찾기
def shark_candidate_position(array, shark_x, shark_y):
    candidate_position = []
    shark_direction = array[shark_x][shark_y][1] # 현재 상어가 바라보고 있는 방향
    # 현재 상어가 바라보고 있는 방향으로 계속 이동시키기
    for _ in range(4): # 최대 4번이동할 수 있음
        shark_x += dx[shark_direction]
        shark_y += dy[shark_direction]
        # 격자안에 있으면서 물고기가 있다면
        if 0 <= shark_x < 4 and 0 <= shark_y < 4 and 1 <= array[shark_x][shark_y][0] <= 16:
            candidate_position.append((shark_x, shark_y))
    return candidate_position


def shark_move(array, ate, shark_x, shark_y):
    global result
    array = copy.deepcopy(array)

    # 지금 상어 자리에 위치했던 물고기 먹기
    ate += array[shark_x][shark_y][0]
    # 상어 자리에 있는 물고기 정보 상어(0)으로 바꾸기
    array[shark_x][shark_y][0] = 0

    # 물고기 이동
    move_fish(array, shark_x, shark_y)

    # 현재 위치에서 상어가 이동가능한 위치 찾기
    candidate_position = shark_candidate_position(array, shark_x, shark_y)

    if len(candidate_position) == 0:
        result = max(result, ate)
        return

    for cand_x, cand_y in candidate_position:
        shark_move(array, ate, cand_x, cand_y)

result = 0
shark_move(array, 0, 0, 0)
print(result)




