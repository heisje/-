import sys

sys.stdin = open('input.txt')
TC = int(input())
for tc in range(1, TC + 1):
    N, *arr = list(map(int, input().split()))
    arr.append(0)
    count = 0
    start = 0
    end = 0 + arr[start]  # 앞으로 가는 최대 위치
    while start <= N-1:
        count += 1
        future = []
        for idx in range(start+1, end+1):  # 갈 수 있는 경우의 수
            future.append((idx + arr[idx], idx))
        end, start = max(future)  # 갈 수 있는 최대 길이를 간다.
        if end >= N-1:
            break
    print(f'#{tc} {count}')