TC = int(input())

ni = [0, 0, -1, 1]
nj = [-1, 1, 0, 0]
for tc in range(TC):
    N = int(input())
    arr = []
    result = 0
    for n in range(N):
        arr.append(list(map(int, input().split())))
    for m in range(N): 
        for n in range(N): 
            sumi = 0
            #print(m,n)
            for i in range(4):
                #print(i)
                pi = n + ni[i]
                pj = m + nj[i]
                if 0 <= pi < N and 0 <= pj < N: 
                    sumi += abs(arr[pj][pi] - arr[m][n])
            result += sumi    
    print(result)
            

    