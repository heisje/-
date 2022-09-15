import sys
sys.stdin = open('input.txt')


# 재귀로 하는 사칙연산
def cal(n):
    if t_type[n] == '+':
        t_type[n] = cal(t_left[n]) + cal(t_right[n]) # 재귀로 가보자
    elif t_type[n] == '-':
        t_type[n] = cal(t_left[n]) - cal(t_right[n])
    elif t_type[n] == '*':
        t_type[n] = cal(t_left[n]) * cal(t_right[n])
    elif t_type[n] == '/':
        t_type[n] = cal(t_left[n]) / cal(t_right[n])
    return int(t_type[n]) # 사칙연산이 아닐경우 int형변환

TC = 10
for tc in range(1, TC + 1):
    N = int(input())
    t_type = [None] * (N + 1)   # 값을 넣을 곳
    t_left = [None] * (N + 1)   # 왼쪽
    t_right = [None] * (N + 1)  # 오른쪽
    for i in range(1, N + 1):
        _, t_type[i], *nodes = input().split()
        if len(nodes) == 2:     # 2개일땐
            t_right[i] = int(nodes[1])
            t_left[i] = int(nodes[0])

    print(f'#{tc} {cal(1)}')





