import sys
sys.stdin = open('input.txt')

def bus(TYPE, START, END):
    stop = set(START, END)
    #타입이 1인 경우
    if TYPE == 1:
        for i in range(START, END):
            stop += i
    if TYPE == 2:
        for i in range(START, END, 2):
            stop += i
    if TYPE == 3:
        if START % 2 == 1:
            for i in range(START, END, 2):
                stop += i
        if START % 2 == 0:
            for i in range(START, END, 2):
                stop += i
    return

TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        TYPE, START, END = map(int, input().split())

