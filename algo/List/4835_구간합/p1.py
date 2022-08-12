import sys
sys.stdin = open('input.txt')

T = int(input())
result = ''      #결과값

for t in range(T):
    N, M = map(int, input().split())     #N만큼 M개
    li = list(map(int, input().split()))

    #최소 최대값 기본값
    sum_max = sum(li[0 : M])
    sum_min = sum(li[0 : M])

    #center를 기준으로 M만큼 체크
    for center in range(0, len(li)-M+1):
        sum_center = sum(li[center:center+M])
        if sum_center > sum_max:
            sum_max = sum_center
        if sum_center < sum_min:
            sum_min = sum_center

    #결과값
    result += f'#{t+1} {sum_max - sum_min}\n'
print(result)