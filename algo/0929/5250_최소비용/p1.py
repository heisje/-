import sys
sys.stdin = open('input.txt')
from collections import deque
import heapq


def pidq():
    visited = [[1000000 for _ in range(N)]for _ in range(N)]
    visited[0][0] = 0
    dq = deque()
    dq.append((0,0))
    while dq:
        x, y = dq.popleft()
        for gx, gy in ((x, y+1), (x+1, y), (x, y-1), (x-1, y)):
            if 0 <= gx < N and 0 <= gy < N:
                if arr[gy][gx] > arr[y][x]:
                    dis = visited[y][x] + arr[gy][gx] - arr[y][x] + 1
                else:
                    dis = visited[y][x] + 1
                if dis < visited[gy][gx]:
                    visited[gy][gx] = dis
                    dq.append((gx, gy))
    return visited[N-1][N-1]


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = list()
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    print(f'#{tc} {pidq()}')