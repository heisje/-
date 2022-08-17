#import sys
#sys.stdin = open('input.txt')

#풀이핵심: 미리 1로 세팅해두고, 위에서부터 값을 넣는다.
#         삼각형의y,x는 y-1 x-1와 y-1 x을 합한 값이다.
TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    triangle = [[1]*n for n in range(1, N + 1)]
    for col in range(2,N):
        for idx in range(1, col):
            triangle[col][idx] = triangle[col - 1][idx - 1] + triangle[col - 1][idx]
    print(f'#{tc}')
    for col in range(N):
        print(*triangle[col])