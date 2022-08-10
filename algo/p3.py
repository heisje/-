TC = int(input())
for tc in range(TC):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    rotate = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    max_count = N
    rotate_count_2 = 1
    count = 1
    angle = 0
    x = 0
    y = 0
    print(arr)

    for i in range(1, N*N+1): #숫자 하나씩 넣자구
        print(f'({x}, {y})',end=" ")
        arr[y][x] = i
        x += dx[angle]
        y += dy[angle]
        count += 1
        if count == max_count: # 카운트가 다 달았을때
            count = 0
            max_count -= 1    
            rotate_count_2 -= 1
            if rotate_count_2 == 0: #2번마다 로테이트하게
                angle += 1
                rotate_count_2 = N
                if angle == 4:
                    angle = 0
            
    print('-------------')
    for m in range(N):
        print(arr[m])
    print('-------------')