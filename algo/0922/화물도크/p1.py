import sys
sys.stdin = open('input.txt')
from collections import deque


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    time = []
    for _ in range(N):
        time.append(list(map(int, input().split())))
    time.sort(key=lambda x: x[1])
    schedule = [time.pop()]
    while time:
        start, end = time.pop()
        if end <= schedule[-1][0]:  # 끝나는 시간 <= 마지막 start ( 스케줄 넣기 )
            schedule.append([start, end])
        else:  # 스케줄 start 바꾸기
            if start > schedule[-1][0]:
                schedule[-1][0] = start


    print(f'#{tc} {len(schedule)}')