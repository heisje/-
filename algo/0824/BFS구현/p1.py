import sys
sys.stdin = open('input.txt')

'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(N):
    while queue:
        v = queue.pop(0)
        print(v)
        for i in nodes[v]:
            if visited[i] == 0:              #아직 안 갔던 곳이라면
                visited[i] += visited[v] + 1 #방문
                queue.append(i)              #나가기


N, NODE = map(int, input().split())

#노드 입력받기
nodes = [[]for _ in range(N + 1)]
string = list(map(int, input().split()))
for n in range(0, NODE*2, 2):
     nodes[string[n + 1]].append(string[n])
     nodes[string[n]].append(string[n + 1])
print(nodes)

visited = [0] * (N + 1) #방문 한 곳
visited[1] = 1          #1번 지점을 미리 방문처리
queue = [1]             #1번 지점에서 시작
bfs(N)
print(visited)