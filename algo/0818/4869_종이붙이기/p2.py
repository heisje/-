import sys
sys.stdin = open('input.txt')

TC = int(input())
result_li = [0, 1]

for tc in range(1, TC + 1):
    N = int(input()) // 10
    for n in range(2, N + 1):
        if len(result_li) <= n :
            if n % 2 == 1:
                result_li.append(result_li[n - 1] * 2 - 1)
            elif n % 2 == 0:
                result_li.append(result_li[n - 1] * 2 + 1)
    print(f'#{tc} {result_li[N]}')