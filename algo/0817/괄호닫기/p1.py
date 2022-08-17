#import sys
#sys.stdin = open('input.txt')

TC = int(input())
stack = []
top = -1
for tc in range(1, TC + 1):
    string = input()
    for st in string:
        if st == '(':
            top += 1
            stack.append('(')
        if st == ')' and top != -1:
            top -= 1
    if top == -1:
        print(f'#{tc} {1}')
    if top != -1:
        print(f'#{tc} {-1}')