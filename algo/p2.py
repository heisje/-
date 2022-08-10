N = int(input())
for tc in range(N):
    arr = list(map(int, input().split()))
    result = 0
    for i in range(1, 1 << len(arr)):
        sumi = 0
        for j in range(len(arr)):
            if i & (1<<j):
                sumi += arr[j]
        if sumi == 0:
            result = 1
    print(result)