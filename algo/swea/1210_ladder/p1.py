import sys
sys.stdin = open('input.txt')

def way(pre_x, pre_y, ladder, N):
    if ladder[pre_y][pre_x - 1] == 1:
        while ladder[pre_y][pre_x - 1] == 1:
            pre_x -= 1

    elif ladder[pre_y][pre_x + 1] == 1:
        while ladder[pre_y][pre_x + 1] == 1:
            pre_x += 1
    if ladder[pre_y-1][pre_x] == 1:
        pre_y -= 1
    return pre_x, pre_y


for ts in range(1, 11):
    _ = int(input())

    #사다리 제작
    N = 100
    ladder = []
    ladder.append([0]*(N+2))
    for _ in range(N):
        ladder.append([0] + list(map(int, input().split())) + [0])
    ladder.append([0] * (N + 2))
    N += 2

    #시작점 설정
    pre_x = 0 # 현재위치
    pre_y = N-2 # 현재위치
    for i in range(N):
        #print(pre_y, i)
        if ladder[pre_y][i] == 2:
            pre_x = i

    #길찾기
    while True:
        pre_x, pre_y = way(pre_x, pre_y, ladder, N)
        if pre_y == 1:
            print(f'#{ts} {pre_x - 1}')
            break


