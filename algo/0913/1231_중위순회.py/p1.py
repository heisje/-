import sys
sys.stdin = open('input.txt')

def in_order(n):
    if lefts[n]:
        in_order(lefts[n])
    print(names[n], end='')
    if rights[n]:
        in_order(rights[n])
for tc in range(1, 11):
    N = int(input())
    names = [None] * (N+1)
    lefts = [None] * (N+1)
    rights = [None] * (N+1)
    for _ in range(N):
        idx, name, *node = list(input().split())
        idx = int(idx)
        names[idx] = name
        node = list(map(int, node))
        if len(node) == 2:
            lefts[idx] = node[0]
            rights[idx] = node[1]
        elif len(node) == 1:
            lefts[idx] = node[0]

    print(f'#{tc} ', end='')
    in_order(1)
    print()

