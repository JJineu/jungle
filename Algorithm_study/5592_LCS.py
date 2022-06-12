from sys import stdin
input = stdin.readline

def main():
    s1 = input().strip()
    s2 = input().strip()
    graph = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

    for i in range(1,len(s1)+1) :
        for j in range(1,len(s2)+1) :
            if s1[i-1] == s2[j-1] :
                graph[i][j] = graph[i-1][j-1]+1
            else:
                graph[i][j] = max(graph[i][j-1], graph[i-1][j])
    
    print(graph[-1][-1])

main()
