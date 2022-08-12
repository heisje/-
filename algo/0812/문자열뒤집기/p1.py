import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC + 1):
    #1
    string = input()
    result = ''
    for i in range(len(string)):
        result += string[-1-i]
    print(f'#{tc} ', end='')
    print(result)

    #2
    result = list(string)
    for i in range(len(string)//2):
        result[i], result[-1-i] = result[-1-i], result[i]

    result2 = ''
    for i in result:
        result2 += i
    print(result2)

    #3
    result = string[::-1]
    print(result)

