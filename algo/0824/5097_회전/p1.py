import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    arr = list(input().split())
    top = 0
    for time in range(M):
        top = (top + 1) % N
    print(f'#{tc} {arr[(top) % N]}')