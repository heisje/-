import sys
sys.stdin = open('input.txt')


def quick_sort(l, r):  # 나눠진 파티션으로 구하기
    if l < r:
        s = partition(l, r)
        quick_sort(l, s - 1)
        quick_sort(s + 1, r)


def partition(l, r):  # 파티션 나누기
    p = arr[l]
    i = l
    j = r
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, N-1)

    print(f'#{tc} {arr[N//2]}')