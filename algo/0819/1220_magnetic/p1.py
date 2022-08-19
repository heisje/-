import sys
sys.stdin = open('input.txt')

TC = 10
for tc in range(1, TC + 1):
    _ = input()

    #입력받기
    grid = []
    for _ in range(100):
        grid.append(list(map(int, input().split())))

    #패턴 [1,1,2,2] [1,2,2] [1,1,1,1,2]
    #1을 만나기전에 2가 나오면 버림
    #2이후로 있는 1이 나오면 버림
    coucuocuount = 0
    for x in range(100):
        check_1 = False # 1을 만났는가?
        check_2 = False # 2를 만났는가?
        stack = []
        count = 0
        for y in range(100):
            if grid[y][x] == 1: #1은 아래로
                check_1 = True
            elif grid[y][x] == 2: #2는 위로
                if check_1 == False:
                    pass
                elif check_1 == True:
                    check_2 = True
                    count += 1
                    check_1 = False # push pop으로 구현할라고 다시...
        coucuocuount += count
    print(f'#{tc} {coucuocuount}')