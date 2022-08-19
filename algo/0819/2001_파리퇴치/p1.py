import sys
sys.stdin = open('input.txt')

TC = int(input())
def my_sum(li):
    sum_all = 0
    for a in li:
        sum_all += a
    return sum_all

def my_max(li):
    max_all = 0
    for a in li:
        if a > max_all:
            max_all = a
    return max_all

for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    grid = []
    for a in range(N):
        grid.append(list(map(int, input().split())))

    all = [] #모든 합계를 넣을 0
    for y in range(N - M + 1):
        for x in range(N - M + 1):
            sumi = 0  #누적 할 sumi
            for in_y in range(M):
                sumi += my_sum(grid[y+in_y][x:x+M])
            all.append(sumi)
    print(f'#{tc} {my_max(all)}')