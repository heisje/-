import sys
sys.stdin = open('input.txt')


def dfs(n, total):
    global result
    if n == N:
        if result > total:
            result = total
        return
    if total > result:
        return
    for m in range(N):
        if visited[m] == 0:
            visited[m] = 1
            dfs(n+1, total + arr[n][m])
            visited[m] = 0

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    visited = [0] * N
    result = 99 * N
    dfs(0, 0)
    print(f'#{tc} {result}')