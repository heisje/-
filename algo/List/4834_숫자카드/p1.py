import sys
sys.stdin = open('input.txt')

#핵심! 딕셔너리로 카운트를 해서 가장 큰 카운트를 가진 값을 저장한다.
T = int(input())
result = ''
for i in range(T):
    _ = int(input())
    li = list(map(int, input())) #리스트로 받아옴
    dic = {}

    # 딕셔너리에 차곡 차곡 넣는다.
    for num in li:
        if dic.get(num) == None: dic[num] = 1 #비어 있을 땐 1을 넣는다.
        else: dic[num] += 1                   #들어 있으면 += 1

    # value의 최대값을 가진 KEY를 구하고, 그 중에서 KEY의 최대값을 구한다.
    maxi_key = li[0]  # 최대값을 가진 KEY
    for key, value in dic.items():
        if value >= dic[maxi_key]: # 최대 갯수를 찾는다.
            if key >= maxi_key:    # 더 큰 숫자면 덮어씌운다.
                maxi_key = key

    #출력 누적
    result += f'#{i + 1} {maxi_key} {dic[maxi_key]} \n'
    #print(dic)
print(result)