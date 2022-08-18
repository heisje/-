import sys
sys.stdin = open('input.txt')

def dfs(s):
    global result
    if s == 99:
        result = 1
        return 1
    for node in nodes[s]:
        if check_li[node] == 0:
            check_li[node] = 1
            dfs(node)

TC = 10
for tc in range(1, 1 + TC):
    TC, NODE_NUM = map(int, input().split())
    string = list(map(int, input().split()))
    nodes = {i:[] for i in range(100)}
    check_li = [0] * 100
    check_li[0] = 1
    result = 0
    for idx in range(0, NODE_NUM*2, 2):
        nodes[string[idx]].append(string[idx + 1])

    dfs(0)
    #print(nodes)
    print(f'#{tc} {result}')