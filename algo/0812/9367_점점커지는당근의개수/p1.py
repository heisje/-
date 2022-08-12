import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    maxcount = 1
    count = 1
    for i in range(1, len(nums)):
        if nums[i-1] < nums[i]:
            count += 1
            if maxcount < count:
                maxcount = count
        else:
            count = 1
    print(f'#{tc} {maxcount}')