import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC+1):
    grid = [[0] * 10 for _ in range(10)]
    N = int(input())
    for i in range(N):
        x1, y1, x2, y2, c = map(int, input().split())
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                grid[y][x] += c
    # print('---')
    print(f'#{tc} ', end='')
    print(sum(grid[y].count(3) for y in range(10)))
    # print('---')
    # for y in range(0, 10):
    #    print(grid[y])

        #for x in range(x1, x2):
