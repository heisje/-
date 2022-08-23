import sys
sys.stdin = open('input.txt')


def sol(n, N, hap):
    if n == N:
        #print(li)
        #print(hap)
        result.append(hap)
        return
    for digit in range(N):
        if ch_li[digit] == 0:
            ch_li[digit] = 1 #체크리스트
            li[n] = digit    #결과리스트
            hap += arr[digit][n] #합계검산
            sol(n + 1, N, hap)
            hap -= arr[digit][n]
            ch_li[digit] = 0

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = []
    for n in range(N):
        arr.append(list(map(int, input().split())))
    #print(arr)
    li = [0] * N
    ch_li = [0] * N
    result = []
    sol(0, N, 0)
    print(f'#{tc} {min(result)}')