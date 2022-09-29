import sys
sys.stdin = open('input.txt')
import heapq


# 노드의 방향대로 D를 구해놓고
# D가 가장 가까운대로 움직이면서
# U를 구한다음
# D를 덮어씌우면서 진행한다.
def dij():
    dis = [[INF for _ in range(N)]for _ in range(N)]  # 거리저장
    u = [[0 for _ in range(N)]for _ in range(N)]  # visited

    minD = INF
    w = (0, 0)
    while True:
        for y in range(N):
            for x in range(N):
                if u[y][x] == 0 and minD > dis[y][x]:
                    minD = dis[y][x]
                    w = (x, y)
        x = w[0]
        y = w[1]
        u[y][x] = 1
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            gx = x + dx
            gy = y + dy
            if 0 <= gx < N and 0 <= gy < N:
                if arr[gy][gx] > arr[y][x]:

                dis[gy][gx] = min(dis[gy][gx] + 1, dis[y][x] + 1)







INF = 1000000
TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = list()
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    print(f'#{tc} {dij()}')