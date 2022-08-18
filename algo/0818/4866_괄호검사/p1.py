import sys
sys.stdin = open('input.txt')

TC = int(input())
BRACKET = ('(', ')', '{', '}')

for tc in range(1, TC + 1):
    string = input()
    stack = []

    for bit in string: #문자열 속에 문자가
        if bit in BRACKET: # 괄호 중 하나이면

            #괄호가 뭔지 tuple에 넣기 # (괄호 종류, 왼인지 오른인지)
            new = (BRACKET.index(bit) // 2, BRACKET.index(bit) % 2)

            if len(stack) == 0: #비어있으면 그냥 넣고
                stack.append(new)
            elif new[0] == stack[-1][0] and (stack[-1][1] == 0 and new[1] == 1):
            #elif 설명      # 분류는 같되,                #왼쪽 다음 오른쪽이 오면
                stack.pop()
            else:
                stack.append(new)
    #print(stack)
    print(f'#{tc} {1 if len(stack) == 0 else 0}')