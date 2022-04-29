#n과m/백트래킹

# from sys import stdin
# input = stdin.readline

n, m = map(int, input().split())
result = []
visited = [False]*(n+1)

def nm(start):
    if len(result) == m:
        print(" ".join(map(str,result)))
        return
    
    for i in range(start, n+1):
        if not visited[i]:
            result.append(i)
            visited[i] = True

            nm(i+1)

            result.pop()
            visited[i] = False

nm(1)