test = int(input())
for test_case in range(test):
    n, m, l = map(int, input().split())
    arr = [0] * (n + 2)  # 값을 저장할 리스트


    for _ in range(m):
        leap_num, number = map(int, input().split())
        arr[leap_num] = number
    while arr[l] == 0:
        for i in range((n//2)+1):
            if arr[2*i] != 0:
                arr[i] = arr[2*i]+arr[2*i+1]



    print(f'#{test_case+1} {arr[l]}')
