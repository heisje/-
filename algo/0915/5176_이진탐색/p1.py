import sys
sys.stdin = open('input.txt')

def deep(l):
    global count
    if l*2 <= N:
        count += tree[l * 2] + tree[l * 2 + 1]
        deep(l*2)
        deep(l*2 + 1)

TC = int(input())
for tc in range(1, TC + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+2)
    for m in range(M):
        leaf_node, num = map(int, input().split())
        tree[leaf_node] = num
    count = 0
    deep(L)

    print(f'#{tc} {count}')



