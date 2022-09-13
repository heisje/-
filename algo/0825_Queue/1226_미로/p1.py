import sys
sys.stdin = open('input.txt')

TC = 10

for tc in range(1, TC + 1):
    N = 16
    _ = int(input())
    arr = []
    start = []
    end = []

    for n in range(N):
        arr.append(list(map(int, input())))
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                start = (y, x)
                arr[y][x] = 0
            elif arr[y][x] == 3:
                end = (y, x)
                arr[y][x] = 0

    #bfs
    queue = [start]
    count = 2
    while queue:
        y, x = queue.pop(0)
        if (y, x) == end or count == N**2 + 1:
            print(f'#{tc} {1}')
            break
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= y+dy < N and 0 <= x+dx < N:
                if arr[y+dy][x+dx] == 0:
                    arr[y+dy][x+dx] = arr[y][x] + 1
                    queue.append((y+dy, x+dx))
    else:
        print(f'#{tc} 0')



