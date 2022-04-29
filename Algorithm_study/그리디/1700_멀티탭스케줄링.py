# https://www.acmicpc.net/problem/1700
# https://alpyrithm.tistory.com/71

import sys
input = sys.stdin.readline
N, K = map(int,input().split())
elec = list(map(int,input().split()))
plug = [0] * N
cnt = 0
num = 0
for idx,val in enumerate(elec) :
    if val in plug : #멀티탭에 해당 전자기기가 이미 꽂혀있을 경우 패스
        pass
    elif 0 in plug : #멀티탭중에 비어있는 칸이 있는경우
        plug[plug.index(0)]=val #비어있는 인덱스값을 찾아서 그 안에 전자기기를 대입한다.
    else : # 멀티탭에 새로운 전자기기가 꼽혀야할경우
        swap = 0
        plug_idx= 0
        for j in plug : # 현재 탭에 꽂혀있는 전자기기를 조사한다.
            if j not in elec[idx:] : # 꼽혀있는 전자기기가 다음에 필요한 전자기기가 아니라면
                swap = j
                break  #탭에 꽂혀있는게 다음에 쓰여지지 않는다면 더이상 탭에 꽂힌걸 탐색할 필요없이 꽂아주면 되기 때문에 break를 사용한다.
            elif elec[idx:].index(j) > plug_idx : # 탭에 꽂혀있는 전자기기 두개가 둘다 뒤에 쓰여질거라면 우선순위를 다음 인덱스(더 나중에 쓰여질) 전자기기를 찾아 그 전자기기값을 탭에 꽂아주는걸로 하기 위함이다.
                plug_idx = elec[idx:].index(j) # 다음 탭과 비교하기 위해 탭인덱스를 저장
                swap = j
        plug[plug.index(swap)] = val
        cnt += 1
print(cnt)

#Pass와 Continue 차이
# https://zetawiki.com/wiki/%ED%8C%8C%EC%9D%B4%EC%8D%AC_pass%EC%99%80_continue_%EC%B0%A8%EC%9D%B4%EC%A0%90
#Enumerate 인덱스값과 밸류값 같이 받을때 유용하게 쓸수 있다. -> 주로 for문에서 쓴다. 그 외...
