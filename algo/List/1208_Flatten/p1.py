import sys
sys.stdin = open('input.txt')

def flatten(N, li):
    for n in range(N):
        li[max(zip(range(0, len(li)), li), key=lambda x:x[1])[0]] -= 1
        li[min(zip(range(0, len(li)), li), key=lambda x:x[1])[0]] += 1
    return max(li)-min(li)

for i in range(10):
    N = int(input())
    li = list(map(int, input().split()))
    print(f'#{i+1} {flatten(N, li)}')
