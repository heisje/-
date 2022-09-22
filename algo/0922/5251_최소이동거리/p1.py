import sys
sys.stdin = open('input.txt')


def dfs(idx, count):
    global mini
    if idx == N:
        if mini > count:
            mini = count
        return
    if mini < count:
        return
    for node, width in nodes[idx]:
        dfs(node, count + width)


TC = int(input())
for tc in range(1, TC + 1):
    N, E = map(int, input().split())
    nodes = [[] for _ in range(N)]
    widths = [[] for _ in range(N)]
    for _ in range(E):
        start, end, width = map(int, input().split())
        nodes[start].append((end, width))
    mini = 1000000 * 10
    dfs(0, 0)
    print(f'#{tc} {mini}')