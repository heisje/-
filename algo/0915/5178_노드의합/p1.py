import sys
sys.stdin = open('input.txt')

def inorder(n):
    global node_num
    if n * 2 <= N:
        inorder(n * 2)
    tree[n] = node_num
    node_num += 1
    if n * 2 + 1 <= N:
        inorder(n * 2 + 1)

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    tree = [0] * (N + 1)
    node_num = 1
    inorder(1)
    #print(tree)
    print(f'#{tc} {tree[1]} {tree[N//2]}')



