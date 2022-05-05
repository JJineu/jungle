#카드놓기/재귀함수
#순열사용
'''
sequence = [["12", "1"], ["2","3"], ["4","5"], ["5","6"]]
for s in sequence:
    print("".join(s))
'''

from itertools import permutations

n = int(input())
k = int(input())
arr =[]
for i in range(n):
    arr.append(input())

temp=[]
card = list(permutations(arr,k))
for i in card:
    temp.append("".join(i))
 
result =[]
for i in temp:
    if i not in result:
        result.append(i)

print(len(result))