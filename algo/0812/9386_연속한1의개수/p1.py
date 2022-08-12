import sys
sys.stdin = open('input.txt')

#핵심! 1을 셀때마다 제일 크면 맥스 카운트를 세준다.
TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    string = input()

    i = 0
    count = 0
    maxcount = 0
    while i <= N - 1:
        if string[i] == '1':
            count += 1
            if maxcount < count:
                maxcount = count
        else:
            count = 0
        i += 1
    print(f'#{tc} {maxcount}')