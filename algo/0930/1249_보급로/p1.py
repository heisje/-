import heapq

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input())))
    q = []
    heapq.heappush(q, (0,0,0))  # 깊이, x, y
    visited = [[100000000 for _ in range(N)] for _ in range(N)]
    visited[0][0] = 0
    while heapq:
        # 가장 작은 위치를 찾는다.
        depth, x, y = heapq.heappop(q)
        # 종료 조건: 도착
        if x == N-1 and y == N-1:
            break
        # 가장 작은 위치에서 이동한다.
        for dx, dy in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
            if 0 <= dx < N and 0 <= dy < N:  # 그리드 안에서
                temp = visited[y][x] + arr[dy][dx]
                if temp < visited[dy][dx]:  # 값이 더 작으면 누적시킨다.
                    visited[dy][dx] = temp
                    # dij에 가장 작은 위치를 적어놓을 곳을 만든다.
                    heapq.heappush(q, (visited[dy][dx], dx, dy))

    print(f'#{tc} {visited[y][x]}')