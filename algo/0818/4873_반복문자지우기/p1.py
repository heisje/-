import sys
sys.stdin = open('input.txt')

save = None
TC = int(input())

for tc in range(1, TC + 1):
    string = input()
    stack = [string[0]]

    for idx in range(1, len(string)):
        if len(stack) == 0:
            stack.append(string[idx])
        elif string[idx] == stack[-1]: #같으면 빼버리고
            stack.pop()
        elif string[idx] != stack[-1]: #같지 않으면 스텍에 넣는다.
            stack.append(string[idx])
    print(f'#{tc} {len(stack)}')