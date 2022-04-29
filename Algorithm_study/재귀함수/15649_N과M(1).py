#N과M(1)/백트래킹

N, M = map(int, input().split())

visited =[False]*(N+1)
result = []

def nm(num):
    if num == 0:
        print(" ".join(map(str,result)))
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            
            nm(num-1)

            visited[i] = False
            result.pop()

nm(M)
