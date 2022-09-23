import sys
sys.stdin = open('input.txt')


# 아이디어 : 1달과 3달로 계~속 분기해서 12를 만드는 순열을 만든다.
def dfs(idx, money_sum):
    global min_money
    if money_sum > min_money:  # 가지치기: 돈이 최솟값보다 커지면 return
        return
    if idx >= 12:              # 종료조건: 12달 초과하면,
        min_money = money_sum  #          이게 가장 작은 money
        return
    dfs(idx + 1, money_sum + money[idx])  # 1달로 분기
    dfs(idx + 3, money_sum + pay[2])      # 3달로 분기

TC = int(input())
for tc in range(1, TC + 1):
    pay = list(map(int, input().split()))       # 가격 # 1일 1달 3달 1년
    schedule = list(map(int, input().split()))  # 수영장 value값
    money = [0] * 12                            # 1달에 비싼 돈

    for idx, value in enumerate(schedule):  # 1일 vs 1달
        if value*pay[0] > pay[1]:
            money[idx] = pay[1]
        else:
            money[idx] = value * pay[0]

    min_money = pay[3]  # 최소 값은 1년권으로 지불했을 때
    dfs(0, 0)

    print(f'#{tc} {min_money}')