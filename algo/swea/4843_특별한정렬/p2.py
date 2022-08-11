TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = []
    arr.sort()

    maxi_idx = 0
    mini_idx = 0

    for a in range(len(arr)):
