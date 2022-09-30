import sys
sys.stdin = open('input.txt')


def solve(y, N, choice):
    global result
    if y == N:
        result += 1
        #print(choice)
        #print(vi_c_rt)
        #print(vi_c_lt)
        return
    for x in range(N):  # x축 하나를 선택한다.
        # 선택해보았는데, visited에 아직 선택 안했으면 pass
        if vi_x[x] == 0 and vi_c_lt[lt_rb[y][x]] == 0 and vi_c_rt[lb_rt[y][x]] == 0:
            vi_x[x] = 1
            vi_c_lt[lt_rb[y][x]] = 1
            vi_c_rt[lb_rt[y][x]] = 1
            solve(y+1, N, choice + f'{x}')
            vi_x[x] = 0
            vi_c_lt[lt_rb[y][x]] = 0
            vi_c_rt[lb_rt[y][x]] = 0


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    result = 0
    lt_rb = [[(n + k) for n in range(N)] for k in range(N)]
    #print(lt_rb)
    lb_rt = [[(n + k) for n in range(N - 1, -1, -1)] for k in range(N)]
    vi_x = [0] * N
    vi_c_lt = [0] * (N*2-1)
    vi_c_rt = [0] * (N*2-1)
    # vi_y = [0] * N
    solve(0, N, '')
    print(f'#{tc} {result}')