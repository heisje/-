import sys
from itertools import combinations

sys.stdin = open('input.txt')
TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    foods = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if y < x:
                foods[y][x] = arr[y][x] + arr[x][y]
    foods_sum = sum(sum(foods[y]) for y in range(N))

    combis = list(combinations([i for i in range(N)], N//2))

    score = []
    for combi in combis:
        sum_foods = 0
        for y in range(N):
            for x in range(N):
                if y < x:
                    if x in combi and y in combi:
                        sum_foods += foods[y][x]

        score.append(abs(sum_foods - (foods_sum-sum_foods)))

    print(f'#{tc} {min(score)}')