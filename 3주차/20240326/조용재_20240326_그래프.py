def solution(edges):
    def count_edges(edges):
        edge_counts = {}
        for a, b in edges:
            # 각 노드별로 간선의 수를 추가할 딕셔너리를 생성 - .get() 함수를 이용해 딕셔너리의 키 값 추가
            if not edge_counts.get(a):
                edge_counts[a] = [0, 0]
            if not edge_counts.get(b):
                edge_counts[b] = [0, 0]

            # output edge와 input edge의 개수를 추가
            edge_counts[a][0] += 1  # a는 n번 노드에서 나가는 간선
            edge_counts[b][1] += 1  # b는 n번 노드로 들어오는 간선
        return edge_counts

    def check_answer(egde_counts):
        answer = [0, 0, 0, 0]
        for key, counts in edge_counts.items():
            # 생성된 정점의 번호 확인
            if counts[0] >= 2 and counts[1] == 0:
                answer[0] = key
            # 막대 모양 그래프의 수 확인
            elif counts[0] == 0 and counts[1] > 0:
                answer[2] += 1
            # 8자 모양 그래프의 수 확인
            elif counts[0] >= 2 and counts[1] >= 2:
                answer[3] += 1
        # 도넛 모양 그래프의 수 확인
        answer[1] = (edge_counts[answer[0]][0] - answer[2] - answer[3])

        return answer

    edge_counts = count_edges(edges)
    answer = check_answer(edge_counts)

    return answer