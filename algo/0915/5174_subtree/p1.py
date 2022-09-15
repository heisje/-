import sys
sys.stdin = open('input.txt')

def deep(node):
    global count
    count += 1
    if nodes.get(node):
        for a in nodes.get(node):
            deep(a)

TC = int(input())
for tc in range(1, TC + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    nodes = dict()
    for i in range(0, E*2, 2):
        start = arr[i]
        end = arr[i + 1]
        if not nodes.get(start):
            nodes[start] = [end]
        else:
            nodes[start].append(end)
    count = 0
    if not nodes.get(N):
        print(f'#{tc} {count + 1}')
    else:
        for node in nodes.get(N):
            deep(node)
        print(f'#{tc} {count + 1}')





