import sys
sys.stdin = open('input.txt')


# baby-gin
# 연속된 3개를 찾는다.
# 제외하고 같은 3개를 찾는다.
TC = int(input())
for tc in range(1, TC + 1):
    arr = list(map(int, input()))
    visited = [0] * len(arr)
    arr.sort()
    count = 0





