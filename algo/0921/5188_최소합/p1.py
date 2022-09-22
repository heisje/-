import sys
sys.stdin = open('input.txt')


def dfs(x, y, count):
    global mini
    if x == N-1 and y == N-1:
        if mini > count:
            mini = count
            return
        if mini == 0:
            mini = count
            return

    if mini < count and mini != 0:
        return
    for dx, dy in [(0, 1), (1, 0)]:
        gox = x + dx
        goy = y + dy
        if 0 <= gox < N and 0 <= goy < N:
            count += arr[goy][gox]
            dfs(gox, goy, count)
            count -= arr[goy][gox]


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = []
    mini = 0
    for n in range(N):
        arr.append(list(map(int, input().split())))
    dfs(0, 0, arr[0][0])
    print(f'#{tc} {mini}')