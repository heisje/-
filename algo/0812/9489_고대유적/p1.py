import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    grid = []

    #입력받기
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    #가로검증
    max_count = 0
    for n in range(N):
        count = 0
        for m in range(M):
            if grid[n][m] == 1:
                count += 1
                if max_count < count:
                    max_count = count
            else:
                count = 0

    #세로검증
    for m in range(M):
        count = 0
        for n in range(N):
            if grid[n][m] == 1:
                count += 1
                if max_count < count:
                    max_count = count
            else:
                count = 0
    print(f'#{tc} {max_count}')
