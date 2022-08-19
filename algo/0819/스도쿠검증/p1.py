import sys
sys.stdin = open('input.txt')

# 검증해야할 칸을 set에 넣어 set의 크기가 9인지 확인한다.
TC = int(input())
for tc in range(1, TC + 1):
    sudoku = []
    result = 1 # True
    for y in range(9):
        sudoku.append(list(map(int, input().split())))

    # 가로검증
    for y in range(9):
        nums = set(sudoku[y])
        if len(nums) != 9:
            result = 0

    # 세로검증
    for x in range(9):
        nums = set()
        for y in range(9):
            nums.add(sudoku[y][x])
        if len(nums) != 9:
            result = 0

    # 박스검증 (모든 칸을 3x3박스로 나눔)
    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            nums = set()
            for in_y in range(3): # 박스안에서 3x3체크
                nums.update(sudoku[y+in_y][x:x+3])
            if len(nums) != 9:
                result = 0

    print(f'#{tc} {result}')
