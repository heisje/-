import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    #총개수, 노드개수
    V, E = map(int, input().split())
    visited = [0] * (V+1)
    nodes = [[] for _ in range(V + 1)]

    #노드정보 저장
    for e in range(E):
        start, end = map(int, input().split())
        nodes[start].append(end)
        nodes[end].append(start)

    #시작점, 엔드점
    S, G = map(int, input().split())
    queue = [S]
    result = 0 #결과
    while queue:
        pre = queue.pop(0) #현재 위치
        if pre == G: #무섭다 수민
            result = visited[pre]
            break
        for node in nodes[pre]:
            if visited[node] == 0:
                visited[node] = visited[pre] + 1
                queue.append(node)
    print(f'#{tc} {result}')
