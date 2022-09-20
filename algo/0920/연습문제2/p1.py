import sys
sys.stdin = open('input.txt')


def check(arr):
    return int('0b'+arr, 2)


def binary(arr):
    n = int(arr)
    sum = 0
    for j in range(7):
        temp = n % 10 # 나머지
        n = n // 10
        sum += temp * 2**j

    return sum


# 16진수 4비트로 변환, 2진수 문자열로 변환, 7비트씩 끊기, 십진수로 변환
TC = int(input())
for tc in range(1, TC + 1):
    arr = input()
    b_arr = ''
    for i in range(len(arr)):
        b_arr += bin(int(arr[i], 16))[2:].zfill(4)

    arr = b_arr

    idx = 0
    LEN = len(arr)
    while idx <= LEN - 1:
        print(check(arr[idx:idx+7]), end=' ')
        #print(binary(arr[idx:idx + 7]), end=' ')
        idx += 7
    print()