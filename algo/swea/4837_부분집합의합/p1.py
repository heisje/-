import sys
sys.stdin = open('input.txt')

#핵심: N개의 len을 가진 list에 숫자를 하나씩 넣어준다.
#     만약 이미 넣어져 있는 숫자면 패스한다.
N, K = map(int, input().split())
arr = [i for i in range(1, N + 1)]
checklist = [True if i <= N else False for i in range(1, 13)]

while True: #넥스트 인덱스를 찾는 과정
    if arr[-1] < 12 and checklist[arr[-1] + 1] == False:
        checklist[arr[-1]] = False
        arr[-1] += 1
        checklist[arr[-1]] = True
    elif arr[-1] == 12:
print(arr)
print(checklist)


