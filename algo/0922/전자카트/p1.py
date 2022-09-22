import sys
sys.stdin = open('input.txt')


def dfs(vi, idx, count):
    if idx == -1:
        result.append(count + arr[vi[idx]][vi[idx+1]])
        return
    for value in range(1, N):
        if value not in vi:
            vi[idx] = value
            dfs(vi, idx-1, count + arr[vi[idx]][vi[idx+1]])
            vi[idx] = -1


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []

    vi = [-1 for _ in range(N)]
    vi[-1] = 0

    dfs(vi, N-2, 0)
    print(f'#{tc} {min(result)}')






