import sys
sys.stdin = open('input.txt')

#아이디어 : 선형 큐 구조를 응용해서 원이 실제로 돌아가진 않는데, 시작점을 변경해주면서 판단한다.
TC = 10

for tc in range(1, TC + 1):
    _ = int(input())
    arr = list(map(int, input().split()))
    #(arr)
    front = 0 #맨앞 참조
    rear = 0 #이게 필요할까?
    cycle = 1 #더해주는 값
    while True:
        arr[front] -= cycle
        if arr[front] <= 0:
            arr[front] = 0
            front = (front + 1) % 8
            break
        front = (front + 1) % 8

        cycle += 1
        if cycle == 6:
            cycle = 1

    print(f'#{tc} ', end='')
    for idx in range(front, front + 8):
        print(arr[idx % 8], end=' ')
    print()

