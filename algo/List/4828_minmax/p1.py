import sys
sys.stdin = open('input.txt')

N = int(input())

for i in range(N):
    LIST_LEN = int(input()) #리스트 길이
    STRING = input()        #문자열 저장
    result = []  #결과 저장


    li_sub = ''  #담아둘 공간
    li = []      #숫자 리스트

    index = 0
    while index < len(STRING):
        if STRING[index] != ' ' and STRING[index] != '\n':
            li_sub += STRING[index]
        else:
            li.append(li_sub)
            li_sub = ''  # 담아둘 공간 초기화
        index += 1
        if index == len(STRING):
            li.append(li_sub)
            li_sub = ''  # 담아둘 공간 초기화

    maxi = 0
    mini = int(li[0])
    for chrr in li:
        intt = int(chrr)
        if maxi < intt:
            maxi = intt
        if mini > intt:
            mini = intt
    print(f'#{i + 1} {maxi - mini}')