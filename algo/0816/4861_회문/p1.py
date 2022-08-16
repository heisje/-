import sys
sys.stdin = open('input.txt')

TC = int(input())

#테스트 케이스 별
for tc in range(1, TC + 1):
    n, m = map(int, input().split())
    str_map = []

    #입력받기
    for nn in range(n):
        str_map.append(input())

    #비교할 구문 저장
    num = n - m + 1 # 라인 하나당 구문 개수
    string = []

    #구문 저장 및 검출
    for nn in range(n):
        #가로 검출
        for idx in range(num):
            test_string = str_map[nn][idx:idx + m]
            if test_string == test_string[::-1]:
                string.append(test_string)

    # 세로 돌려서 검출
    reverse_str_map = [[row[i] for row in str_map] for i in range(len(str_map[0]))]
    for nn in range(n):
        for idx in range(num):
            test_string = reverse_str_map[nn][idx:idx + m]
            if test_string == test_string[::-1]:
                string.append(''.join(test_string))

    # 출력
    print(f'#{tc} ', end='')
    print(*string)

