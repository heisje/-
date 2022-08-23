import sys
sys.stdin = open('input.txt')

rank = {'(': [0, 3],
        '+': [1, 1],
        '*': [2, 2],
        }

TC = 10
for tc in range(1, TC + 1):
    N = input()
    string = input() + ')'
    s_opr = ['(']
    postfix = []

    for temp in string:
        if temp.isdigit(): #숫자 면
            postfix.append(temp)
            #print(temp, end='')
        else: #숫자가 아니면
            if temp == ')':
                while True: # ( 나올때 까지 무한 pop
                    if s_opr[-1] == '(':
                        s_opr.pop()
                        break
                    else:
                        postfix.append(s_opr.pop())
            else:
                if rank[temp][1] > rank[s_opr[-1]][0]: #새로 들어온게 더 크면
                    s_opr.append(temp)
                else: #작거나 같으면
                    while rank[temp][1] < rank[s_opr[-1]][0]:
                        postfix.append(s_opr.pop())
                    s_opr.append(temp)
    #print(postfix)
    s_num = []
    for temp in postfix:
        if temp.isdigit():
            s_num.append(int(temp))
        else:
            num_1 = s_num.pop()
            num_2 = s_num.pop()
            if temp == '+':
                s_num.append(num_1 + num_2)
            elif temp == '*':
                s_num.append(num_1 * num_2)
    print(f'#{tc} ', end='')
    print(*s_num)



