import sys
sys.stdin = open('input.txt')


d_y = (0, -1, 1, 0, 0)  # 상, 하, 좌, 우
d_x = (0, 0, 0, -1, 1)  # 상, 하, 좌, 우

TC = int(input())
for tc in range(1, TC + 1):
    N, M, K = map(int, input().split())  # N = 정사각형 크기, M = 시간, K = 미생물 군집의 개수
    arr = [[[] for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        y, x, value, way = map(int, input().split())
        arr[y][x].append({
            'value': value,
            'way': way,
            'time': 0
        })
    for time in range(M):
        for y in range(N):
            for x in range(N):
                #print(x, y)
                if arr[y][x] == []:       # 비어있으면 넘어가
                    continue
                if arr[y][x][0]['time'] != time:  # 이미 행동했으면 안해
                    continue
                way = arr[y][x][0]['way']
                go_x = x + d_x[way]
                go_y = y + d_y[way]
                arr[y][x][0]['time'] += 1

                if go_x == 0 or go_x == N-1 or go_y == 0 or go_y == N-1:
                    # 방향 바꿔주기 1->2 2->1 3->4 4->3
                    if arr[y][x][0]['way'] == 1: arr[y][x][0]['way'] = 2
                    elif arr[y][x][0]['way'] == 2: arr[y][x][0]['way'] = 1
                    elif arr[y][x][0]['way'] == 3: arr[y][x][0]['way'] = 4
                    elif arr[y][x][0]['way'] == 4: arr[y][x][0]['way'] = 3
                    arr[y][x][0]['value'] = arr[y][x][0]['value'] // 2
                    if arr[y][x][0]['value'] == 0:
                        arr[y][x].pop(0)
                        continue

                arr[go_y][go_x].append(arr[y][x][0])
                arr[y][x].pop(0)

        for y in range(N):
            for x in range(N):
                if len(arr[y][x]) > 1:  # 해당 칸에 중복 계산
                    max_value = 0
                    max_idx = 0
                    sum_value = 0
                    for idx in range(len(arr[y][x])):
                        sum_value += arr[y][x][idx]['value']
                        if max_value < arr[y][x][idx]['value']:
                            max_idx = idx
                            max_value = arr[y][x][idx]['value']
                    arr[y][x] = [{
                        'value': sum_value,
                        'way': arr[y][x][max_idx]['way'],
                        'time': arr[y][x][max_idx]['time']
                    }]

    sum_value = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x]:
                sum_value += arr[y][x][0]['value']
    #print('time', time)
    #for n in range(N):
    #    print(arr[n])
    print(f'#{tc} {sum_value}')