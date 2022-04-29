#한수/수학
N = int(input())
count = 0

if N <100:
    print(N)
else:
    count =99
    for i in range(100,N+1):

        k = str(i)
        if int(k[0])-int(k[1]) ==int(k[1])-int(k[2]):
            count +=1
    print(count)

