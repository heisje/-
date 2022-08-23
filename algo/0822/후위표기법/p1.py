import sys
sys.stdin = open('input.txt')

dic = {'(':[0, 3], '+':[1, 1], '-':[1, 1], '*':[2, 2], '/':[2, 2], ')':[10, 10]}

TC = int(input())
for tc in range(1, TC + 1):
    string = list(input())+[')']
    result = []
    stack_operator = ['(']
    for temp in string:
        if '0' <= temp <= '9': #숫자일 경우
            result.append(temp)
        else:                  #문자일 경우
            if temp == ')':    #)가 들어왔을 경우는 (가 나올 때 까지 전부 Pop
                while True:
                    if stack_operator[-1] == '(':
                        stack_operator.pop()
                        break
                    else:
                        result.append(stack_operator.pop())
            elif dic[temp][1] > dic[stack_operator[-1]][0]: # 들어올 것과 마지막 스텍을 비교하여 우선순위가 높으면 push()
                stack_operator.append(temp)
            else:
                while True: # 새로들어온것보다 작거나 같으면 전부 pop
                    if dic[temp][1] <= dic[stack_operator[-1]][0]:
                        result.append(stack_operator.pop())
                    else:
                        break
                stack_operator.append(temp) #새로 들어온 것 추가

    print(''.join(result))