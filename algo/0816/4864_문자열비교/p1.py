import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC + 1):
    str1 = input()
    str2 = input()
    print(f'#{tc} {1 if str1 in str2 else 0}')