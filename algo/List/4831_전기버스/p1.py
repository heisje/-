import sys
sys.stdin = open('input.txt')

#핵심!: 두번째 정거장 갈 여유되면 무조건 나중에 간다~
N = int(input())
for case in range(N):
    #타임은 충전시 가는 길이, END는 마지막 종점
    TIME, END, _ = map(int, input().split())
    charge = list(map(int, input().split())) + [END]

    pre_x = 0  #현재위치
    count = 0  #카운트 세기

    #체크하는데, 정류장마다 검사하기
    for i in range(len(charge)-1):
        if pre_x + TIME >= charge[i + 1]: #두번째 정거장에 갈 여유 있을 때
            pass
        elif pre_x + TIME >= charge[i]:  #여유는 없는데 충전하면 될 때
            pre_x = charge[i]
            count += 1
        else:                            #모자랄 때 0
            count = 0
            break
    if pre_x + TIME < END:  # 마지막 정거장에 도착했을 때
        count = 0

    print(f'#{case+1} {count}')