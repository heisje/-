import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0]
    for i in range(len(arr)):
        heap.append(arr[i])
        i = i+1
        while 1 <= i:
            if heap[i] < heap[i//2]:
                heap[i], heap[i//2] = heap[i//2], heap[i]
            i = i//2
    i = (len(heap)-1)//2
    count = heap[i]
    while i >= 2:
        i = i//2
        count += heap[i]

    print(f'#{tc} {count}')