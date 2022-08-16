import sys
sys.stdin = open('input.txt')

def brute_force(li, re_li, n):
    num = 100 - n + 1
    for col in range(0, 100):
        for idx in range(0, num):
            if li[col][idx:idx + n] == li[col][idx + n - 1:idx - 1:-1]: # 가로의 모든 횟수
                return True
            if re_li[col][idx:idx + n] == re_li[col][idx + n - 1:idx - 1:-1]: # 세로의 모든 횟수
                return True
    return False

TC = 10

for tc in range(1, 1 + TC):
    _ = input()
    #입력받기
    big_map = []
    for _ in range(100):
        big_map.append(input())
    re_big_map = list(zip(*big_map))

    #검출
    for n in range(100, 1, -1):
        #print(n)
        if brute_force(big_map, re_big_map, n):
            print(f'#{tc} {n}')
            break



