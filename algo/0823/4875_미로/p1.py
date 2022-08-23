import sys
sys.stdin = open('input.txt')

dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    global find
    if miro[y][x] == '2':
        find = 1
        return
    else:
        miro[y][x] = '-1'
        for xy in dxdy:
            if 0 <= y + xy[1] < N and 0 <= x + xy[0] < N:
                if miro[y + xy[1]][x + xy[0]] == '0' or  miro[y + xy[1]][x + xy[0]] == '2' :
                    dfs(x + xy[0], y + xy[1])

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())

    #미로, 시작위치 입력받기
    miro = []
    x = y = -1
    for t_y in range(N):
        temp = input()
        t_x = temp.find('3') # x위치를 찾아본다.
        if t_x != -1:        # x위치가 존재하면 save
            x, y = t_x, t_y
        miro.append(list(temp))

    find = 0
    dfs(x, y)
    print(f'#{tc} {find}')


