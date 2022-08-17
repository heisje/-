#import sys
#sys.stdin = open('input.txt')
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


#input
N, _ = map(int, input().split())
string = list(map(int, input().split()))
check_li = [False] * (N) 
stack = []
visited = []
#딕셔너리로 변경
node_map = {i:[] for i in range(N)}
for idx in range(0, len(string), 2):
    node_map[string[idx] - 1].append(string[idx + 1] - 1)
    node_map[string[idx + 1] - 1].append(string[idx] - 1)

#방문점 0 설정
pre = 0 #현재위치
visited.append(pre)
check_li[pre] = True
while True:
    while len(node_map[pre]) > 0:    #맵의 갈 곳이 남아있는 경우
        target = node_map[pre].pop(0)   #현재위치의, 갈수있는곳 중 가장 작은 수를 pop한다.
        if check_li[target] == False:    #안갔던 곳이면
            stack.append(pre)
            check_li[target] = True            #갔다고 체크!
            visited.append(target)
            pre = target
            break
        elif check_li[target] == True:   #갔던 곳이면
            pass                            #넘어가자!
    else:                          #갈 곳이 남아있지 않은 경우
        if len(stack) > 0:     
            pre = stack.pop()
        else:                   #스텍이 비어있으면
            break  
for vi in visited:
    print(vi + 1, end=' ')
'''
1. 방문한다.
2. 방문할 곳이 비어있지 않으면
    3. 방문해서 가장 숫자가 낮은 곳을 pop한다.
        4. 안갔던 곳이면 갔다고 체크해야한다.
        4. 갔던 곳이면 pop만 하고, 안갔던 곳을 찾는다.
2. 방문할 곳이 비어있으면
    3. stack에서 꺼내와서 방문지점으로 삼는다.
3. 갈 곳이 남아있으면 stack에 넣는다.
'''
