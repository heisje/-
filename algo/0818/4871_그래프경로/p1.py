import sys
sys.stdin = open('input.txt')

def dfs(s):
    while True:
        #print('s: ', s)
        #print('stack: ', stack)
        if s == G: # 도착점에 왔으면!
            return 1
        for idx, node in enumerate(node_dic[s]): # 시작점에서 길찾기
            if visited[node] == 1:
                pass
            if visited[node] == 0:
                stack.append(s)
                s = node
                visited[s] = 1
                break
        else:
            if len(stack) >= 1:
                s = stack.pop()
            else:
                return 0

TC = int(input())
for tc in range(1, TC + 1):
    V, E = map(int, input().split())
    node_dic = {i:[] for i in range(V+1)}
    visited = [0] * (V + 1)
    stack = []
    for _ in range(E):
        start, end = map(int, input().split())
        node_dic[start].append(end)
    S, G = map(int, input().split())
    #print('node', node_dic)
    print(f'#{tc} {dfs(S)}')