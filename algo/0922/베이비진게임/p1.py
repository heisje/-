import sys

sys.stdin = open('input.txt')
TC = int(input())
for tc in range(1, TC + 1):
    turn = list(map(int, input().split()))

    p1 = [0 for _ in range(20)]
    p2 = [0 for _ in range(20)]
    for idx in range(0, len(turn), 2):
        p1_card = turn[idx]
        p2_card = turn[idx + 1]

        p1[p1_card] += 1
        #p1[p1_card + 10] += 1
        p2[p2_card] += 1
        #p2[p2_card + 10] += 1

        if 3 in p1:
            print(f'#{tc} {1}')
            break
        count = 0
        for i in range(20):
            if p1[i] > 0:
                count += 1
                if count == 3:
                    break
            else:
                count = 0
        if count == 3:
            print(f'#{tc} {1}')
            break

        count = 0
        if 3 in p2:
            print(f'#{tc} {2}')
            break
        for i in range(20):
            if p2[i] > 0:
                count += 1
                if count == 3:
                    break
            else:
                count = 0
        if count == 3:
            print(f'#{tc} {2}')
            break
    else:
        print(f'#{tc} {0}')