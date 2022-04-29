# https://www.acmicpc.net/problem/5639

from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline

def postorder(nums):
    length = len(nums)

    if length <= 1:
        return nums

    for i in range(1, length):
        if nums[i]> nums[0]:
            return postorder(nums[1:i]) + postorder(nums[i:]) + [nums[0]]
    return postorder(nums[1:]) + [nums[0]]

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

res = []
res = postorder(preorder)
for i in res:
    print(i)


# 인터넷

# from sys import stdin 
# input = stdin.readline

# #입력받을 원소 리스트
# num_list=[]
# while True:
#     try:
#         num=int(input())
#         num_list.append(num)
#     except:
#         break

# def postorder(left,right):
#     #순서 역전시 종료
#     if left>right:
#         return
#     else:
#         mid=right+1        #분할 기준
#         for i in range(left+1,right+1):
#             #해당 원소가 현재 노드보다 크다면 그 전까지는 왼쪽 서브 트리,
#             #해당 원소 이후는 오른쪽 서브 트리이다.
#             if num_list[left]<num_list[i]:
#                 mid=i
#                 break
#         postorder(left+1,mid-1)
#         postorder(mid,right)
#         print(num_list[left])

# postorder(0,len(num_list)-1)


# 동준
import sys
sys.setrecursionlimit(10**6)
input =sys.stdin.readline
def postorder(start, end):
    if start > end:
        return
    root = preorder[start]
    idx = start + 1
    while idx <= end:
        if preorder[idx] > root:
            break
        idx += 1
    postorder(start+1, idx-1)
    postorder(idx, end)
    print(root)
preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break
postorder(0,len(preorder)-1)


# 기성

import sys
sys.setrecursionlimit(10**6)

def postorder(nums):
    length = len(nums)

    if length <= 1:
        return nums

    for i in range(1, length):
        if nums[i] > nums[0]:
            return postorder(nums[1:i]) + postorder(nums[i:]) + [nums[0]]
    return postorder(nums[1:]) + [nums[0]]

preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break

preorder = postorder(preorder)

for n in preorder:
    print(n)
