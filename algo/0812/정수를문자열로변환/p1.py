import sys
sys.stdin = open('input.txt')

for tc in range(1, 7):
    a = int(input())
    #print(a)

    b = ''
    while a > 0:
        b = chr(ord('0') + a % 10) + b #뒤 부터
        a = a // 10
    print(f'{b} {type(b)}')