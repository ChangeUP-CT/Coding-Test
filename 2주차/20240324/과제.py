
def solution(info, edges):
    answer = 0

    def dfs(sheep, wolf):
        nonlocal answer

        print(sheep, wolf,answer)
        if (sheep > wolf) and (answer < sheep):
            answer = sheep
        else:
            return

        for par, child in edges:
            print(par, child)
            if visited[par] and not visited[child]:
                visited[child] = 1
                if info[child] == 0:
                    sheep += 1
                else:
                    wolf += 1
                dfs(sheep, wolf)
                visited[child] = 0

    visited = [0] * len(info)
    visited[0] = 1
    dfs(1,0)

    return answer