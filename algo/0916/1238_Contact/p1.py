import sys
sys.stdin = open('input.txt')
from collections import defaultdict, deque

TC = 10
for tc in range(1, TC + 1):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))
    nodes = defaultdict(list)
    visited = defaultdict(int)
    for n in range(0, N, 2):
        node_from, node_to = arr[n], arr[n+1]
        nodes[node_from].append(node_to)

    dq = deque()
    dq.append(start)
    visited[start] = 1
    max_num = 0
    max_visited = 1
    while dq:
        n = dq.popleft()
        for node in nodes[n]:
            if visited[node] == 0:
                visited[node] = visited[n] + 1
                if visited[node] > max_visited:
                    max_visited = visited[node]
                    max_num = node
                elif visited[node] == max_visited:
                    if max_num < node:
                        max_num = node
                dq.append(node)

    print(f'#{tc} {max_num}')



