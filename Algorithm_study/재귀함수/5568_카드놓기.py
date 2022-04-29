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
s =[]
for i in range(n):
    s.append(input())

SSS=[]
sss = list(permutations(s,k))
for i in sss:
    SSS.append("".join(i))
 
SSS_result =[]
for i in SSS:
    if i not in SSS_result:
        SSS_result.append(i)

print(len(SSS_result))