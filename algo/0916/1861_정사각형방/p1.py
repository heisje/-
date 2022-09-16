import sys
from collections import deque
sys.stdin = open('input.txt')
TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    result = []
    for by in range(N):
        for bx in range(N):
            dq = deque()
            maxi = 0
            visited = [[0] * N for _ in range(N)]
            visited[by][bx] = 1
            dq.append((bx, by))
            while dq:
                x, y = dq.popleft()
                for gy, gx in [(y, x+1), (y, x-1), (y+1, x), (y-1, x)]:
                    if 0 <= gx < N and 0 <= gy < N and visited[gy][gx] == 0:
                        if arr[gy][gx] == arr[y][x] + 1:
                            visited[gy][gx] = visited[y][x] + 1
                            if visited[gy][gx] > maxi:
                                maxi = visited[gy][gx]
                            dq.append((gx, gy))
            #print(visited)
            result.append((maxi, arr[by][bx]))

    m, v = max(result, key=lambda x: x[0])
    result2 = []
    for re in result:
        if m == re[0]:
            result2.append(re[1])
    #print(result)
    #print(result2)
    print(f'#{tc} {min(result2)} {m}')