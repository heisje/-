import sys
sys.stdin = open('input.txt')

'''
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .
'''

TC = int(input())
for tc in range(1, TC+1):
    arr = list(input().split())
    stack = []
    try:
        for temp in arr:
            if temp == '.':
                if len(stack) > 1:
                    result = 'error'
                else:
                    result = stack.pop()
            elif temp not in ['+', '-', '*', '/']:
                stack.append(int(temp))
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                if temp == '+':
                    stack.append(t2 + t1)
                elif temp == '-':
                    stack.append(t2 - t1)
                elif temp == '*':
                    stack.append(t2 * t1)
                elif temp == '/':
                    stack.append(int(t2 / t1))
        print(f'#{tc} {result}')
    except:
        print(f'#{tc} error')

