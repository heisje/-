import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC + 1):
    str1 = list(set(input()))
    str2 = input()
    print(f'#{tc} {max(str2.count(str1[i]) for i in range(len(str1)))}')