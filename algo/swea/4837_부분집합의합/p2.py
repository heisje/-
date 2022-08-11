import sys
sys.stdin = open('input.txt')

TESTCASE = int(input())
for tc in range(1, TESTCASE + 1):
    N, K = map(int, input().split())
    arr = [i for i in range(1, 13)]
    count = 0
    for i in range(1, 1 << 12):
        sumi = 0
        if bin(i).count('1') == N:
            for j in range(12):
                if i & (1 << j):
                    sumi += arr[j]
                    #print('arr=' + str(arr[j]), end=", ")
                    if sumi > K:
                        break
            #print(sumi)
            if sumi == K:
                count += 1
                #print(bin(i))
    else:
        print(f'#{tc} {count}')
    #print('--------------')