import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    tuple_li = []
    for _ in range(N):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s
        if s % 2 == 0:
            s -= 1
        if e % 2 == 0:
            e -= 1
        tuple_li.append((s, e))

    maxi = 0
    for node in range(401):
        count = 0
        for tu in tuple_li:
            if tu[0] <= node <= tu[1]:
                count += 1
        if count > maxi:
            maxi = count
    print(f'#{tc} {maxi}')
