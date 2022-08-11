import sys
sys.stdin = open('input.txt')

def binary(l, r, FIND):
    center = int((l + r) / 2)
    if center == FIND:
        return 1
    elif center > FIND:
        r = center
    elif center < FIND:
        l = center
    return binary(l, r, FIND) + 1

TC = int(input())
for tc in range(1, TC+1):
    P, A, B = map(int, input().split())
    a = binary(1, P, A)
    b = binary(1, P, B)
    if a < b: print(f'#{tc} A')
    elif b < a: print(f'#{tc} B')
    elif b == a: print(f'#{tc} 0')
