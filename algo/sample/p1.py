import sys
from collections import deque
sys.stdin = open('input.txt')
TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    foods = []
    for y in range(N):
        for x in range(N):
            if y < x:
                print(x, y)
                foods.append([arr[y][x] + arr[x][y], x, y])

    print(foods)
    print(f'#{tc} {1}')