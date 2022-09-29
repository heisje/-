import sys
sys.stdin = open('input.txt')


# 부모를 찾는 함수
def find_set(i):
    while i != rep[i]:
        i = rep[i]
    return i


# 합치는 함수
def union(i, j):
    rep[find_set(j)] = find_set(i)


TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    rep = [i for i in range(N + 1)]
    for m in range(0, M*2, 2):
        union(arr[m], arr[m+1])

    count = 0
    for idx, value in enumerate(rep):
        if idx == value:
            count += 1
    print(rep)

    print(f'#{tc} {count - 1}')