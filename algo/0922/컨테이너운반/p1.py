import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort()
    truck.sort()
    result = 0  # 결과값
    m = M-1     # 트럭 index 뒤에서 부터 참조
    while container and m >= 0:  # container와 truck이 둘다 들어있어야 함
        weight = container.pop()  # 가장 무거운 무게를 꺼냄
        if truck[m] >= weight:  # 트럭보다 가벼워면
            m -= 1              # 다음 트럭
            result += weight

    print(f'#{tc} {result}')