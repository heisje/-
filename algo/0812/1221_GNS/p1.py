import sys
sys.stdin = open('input.txt')

check=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

TC = int(input())
for tc in range(1, TC + 1):
    _ = input()
    string = input() #입력받는 길다란 문자열
    save = [0] * 10
    #검증
    for i in range(0, len(string), 4):    #문자열의 첫글짜만 탐색한다.
        for idx, ch in enumerate(check):                  #모든 알파벳 참색
            if ch[0] == string[i]:        #첫글자 비교
                if ch[1] == string[i + 1]:#둘째 글자 비교
                    save[idx] += 1
    print(f'#{tc}')
    for idx, ch in enumerate(check):
        print((ch + ' ') * save[idx], end=' ')
    print()
