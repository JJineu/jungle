#숫자의개수/배열
a = int(input())
b = int(input())
c = int(input())

listA = list(map(int, str(a*b*c)))

count = 0
for i in range(0,10):
    # for j in len(listA):
    #     if listA[j] == i:
    #         count += 1
    #     print(count)
    print(listA.count(i))

# list.count() 리스트에 몇개 들어가있는지