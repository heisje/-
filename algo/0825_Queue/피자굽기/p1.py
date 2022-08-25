import sys
sys.stdin = open('input.txt')




TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = list(map(list, zip(arr, range(M))))

    fire = [] #화덕 생성

    for n in range(N):  # 초기화덕
        fire.append(arr.pop(0))
    #print(arr)
    #print(fire)
    while len(fire) > 1:
        # 피자를 뺄 때 # 남는 피자가 있으면 넣는다.
        if fire[0][0] == 0:
            fire.pop(0)
            if len(arr) > 0:
                temp = arr.pop(0)
                fire.append([temp[0]//2,temp[1]])
        temp = fire.pop(0)
        temp = [temp[0]//2, temp[1]]
        fire.append(temp)
    print(f'#{tc} {fire[0][1] + 1}')