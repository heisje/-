T = int(input())
for tc in range(1, T+1):
    a = float(input())
    result = ''
    for i in range(1, 13):
        if a >= 2**(-i):  # 남은 a의 값이 소수보다 크면
            a -= 2**(-i)  # 그 값을 빼주고,
            result += '1' # 1을 문자열에 더함
        else:
            result += '0' # 0을 문자열에 더함
        if a == 0:
            print(f'#{tc} {result}')
            break
    else:
        print(f'#{tc} overflow') # break문에 안걸리면 overflow