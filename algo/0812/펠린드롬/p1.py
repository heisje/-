import sys
sys.stdin = open('input.txt')

TC = 3
for _ in range(TC):
    string = input()
    print(string, string[::-1])
    if string == string[::-1]:
        print('this is 펠린드롬')
    else:
        print('낫펠린드롬')