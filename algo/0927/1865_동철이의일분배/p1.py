import sys
sys.stdin = open('input.txt')


def dfs(n, total):  # n=인덱스, total=누적 곱
    global maxi  # 최대값
    if n == N:
        if maxi < total:  # 보경이는 if문 없이 했던데..
            maxi = total
        return
    if (1 ** (N - n)) * total <= maxi:  # 가지치기, 나머지가 다 100퍼가 됐을때 작으면 (1 ** (N - n))는 생략가능
        return
    for job in range(N):
        if arr[n][job] != 0 and job_visited[job] == 0:  # 0일때는 볼 필요 없이 0이니까 패스, visited를 써서 본다.
            job_visited[job] = 1
            dfs(n+1, total * (arr[n][job] / 100))
            job_visited[job] = 0


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = [[]for _ in range(N)]
    job_visited = [0 for _ in range(N)]
    for n in range(N):
        arr[n] = list(map(int, input().split()))
    maxi = 0
    dfs(0, 1)
    print('#%d %6f' % (tc, maxi * 100))