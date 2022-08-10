#핵심! =
#달팽이는 나선형을 그린다.
#나선형을 직선으로 N개만큼 그리면 그 다음은 아래로 N-1...
#[N, N-1, N-1, N-2, N-2, ... 1, 1(N-(N-1))]
#개수 2 * (N - 1) + 1
dx = [1, 0, -1, 0] #델타 탐색 (우, 하, 좌, 상)
dy = [0, 1, 0, -1]

TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    arr = [[0] * (N ) for _ in range(N)]

    minus = 0  #N에서 빼는 숫자
    x = 0 #현재위치
    y = 0 
    count = 0 #넣을 숫자
    for i in range(2*(N - 1)+1):   #방향 별 개수의 총 합 만큼
        for j in range(N + minus): #직진 거리 탐색
            count += 1
            arr[y][x] = count
            if j < N + minus -1:
                x += dx[i % 4] #i가 4의 배수에 따라 방향이 바뀜
                y += dy[i % 4]  
            else:
                x += dx[(i+1) % 4] #i가 4의 배수에 따라 방향이 바뀜
                y += dy[(i+1) % 4]  
        minus -= (i+1) % 2 # i가 0, 2, 4, 6일때 갯수를 줄임

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])

