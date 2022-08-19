import sys
sys.stdin = open('input.txt')

def find_x(li, N, M):
    result = 0 # 최종 합계
    count = 1 # 누적 카운트
    for x in range(1, N):
        if li[x - 1] == 1 and li[x] == 1: #이전께 1이고 이번것도 1이면
            count += 1
        if li[x] == 0 and count == M: #0에 도착했을때 카운터가 같으면
            result += 1
        if li[x] == 0:
            count = 1
    if count == M: #
        result += 1
    return result

TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
    rev_gird = list(zip(*grid))

    sumi = 0
    for y in range(N):
        sumi += find_x(grid[y], N, M)
        sumi += find_x(rev_gird[y], N, M)

    print(f'#{tc} {sumi}')
    #가로검증

