import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC + 1):
    string, keyword = input().split()
    result = len(string) - string.count(keyword) * len(keyword) + string.count(keyword)
    print(f'#{tc} {result}')