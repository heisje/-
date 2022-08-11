import sys
sys.stdin = open('input.txt')

def maxi(li):
    maxx = li[0]
    #print(f'li: {li}')
    idx = 0
    for j in range(1, len(li)):
        if li[j] > maxx:
            maxx = li[j]
            idx = j
    return idx

def mini(li):
    minn = li[0]
    #print(f'li: {li}')
    idx = 0
    for j in range(1, len(li)):
        if li[j] < minn:
            minn = li[j]
            idx = j
    return idx

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = []
    for i in range(0, 5, 2):
        maxi_key = maxi(arr[i:])
        arr[i], arr[i+maxi_key] = arr[i+maxi_key], arr[i]
        mini_key = mini(arr[i + 1:])
        arr[i+1], arr[i+1+mini_key] = arr[i+1+mini_key], arr[i+1]
    print(f'#{tc} ',end='')
    print(*arr[0:10])

    # maximum = maxi(arr[i:])
    # print(maximum)
    # #maximum = maxi(arr[i:])
    # #print(minimum)
    # arr[i], arr[maximum] = arr[maximum], arr[i]
    # #arr[i+1], arr[minimum] = arr[minimum], arr[i+1]
