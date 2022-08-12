import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
for tc in range(1, 11):
    _ = input()
    check = input()
    string = input()
    count = 0
    for i in range(len(string) - len(check) + 1):
        for j in range(len(check)):
            if check[j] == string[i+j]:
                pass
            else:
                break
        else:
           count += 1

    print(f'#{tc} {count}')
