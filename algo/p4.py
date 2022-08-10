import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = []
    for m in range(100):
        arr.append(list(map(int,input().split())))

    sumi = []
    for m in range(100):
        sumi.append(sum(arr[m]))

    for n in range(100):
        sum_y = 0
        for m in range(100):
            sum_y += arr[m][n]
        sumi.append(sum_y)

    sum_slice = 0
    for n in range(100):
        sum_slice += arr[n][n]
        sum_slice += arr[n][99-n]
    sumi.append(sum_y)
    print(f'#{tc} {max(sumi)}')