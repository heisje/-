import sys
sys.stdin = open('input.txt')

# 1짜리와 2짜리를 더해서 원하는 길이를 만드는 방법
# 1. 30의 경우 3을 만들어야한다고 치고,
# 2. 1만으로 만드는 방법은 +1 고정
# 3. 1과 2를 포함해서 3을 만드는 법을 구한 뒤, 두배(제곱)를 해서 구한다.
result_li = []
count_li = 0
# 순열로 풀 수 있다...아마
def Repetition(idx, li, N, two, check_li):
    #순열의 가장 작은 숫자부터 큰 숫자까지 ex) 0 0 0 1 ~ 1 1 1 1
    global count_li
    if idx == N:
        if li.count(1) == two:
            count_li += 1
            print(li)
        return
    for num in range(2):
        check_li[idx] = 1
        if check_li.count(1) > 2: #이미 1이 2이상일 경우
            check_li[idx] = 0
        if check_li.count(1) <= 2:
            li.append(num)             #정답 리스트에 넣어준다.
            Repetition(idx + 1, li, N, two, check_li)
            li.pop()
            check_li[idx] = 0
TC = int(input())
for tc in range(1, TC + 1):
    N = int(input()) // 10
    result = 0
    #2의 개수가 N//2개부터 1개 까지 검사
    for two in range(N//2, 0, -1):
        count_li = 0
        one = N - 2 * two
        #print('two: ', two, ',  one:', one)
        check_li = [0] * (one + two)
        Repetition(0, [], len(check_li), two, check_li)
        result += count_li * 2**two
        #print(count_li)
        #print(result)
    #2진법 검사....

    print(f'#{tc} {result + 1}')
