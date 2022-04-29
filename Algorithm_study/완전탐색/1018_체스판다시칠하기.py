# 체스판 다시 칠하기
# 브루트포스 알고리즘


# 체스판은 wbwbwbwb / bwbwbwbw 반복
# 자를 곳을 찾아야하는데 전부다 바꿔버리고 카운트, min값 구하기

from re import L


n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())

#board[i][j]
# 8x8판으로 보기 ,왼쪽위 기준지점 찾기
cnt = 8*8 #최소값이 64개보다는 적을것이므로 임의로 64로 지정
for i in range(n):
    if n-i>=8:
        for j in range(m): #2중 포문을 이용하여 8x8 체스판의 왼쪽위 기준점 잡기
            chk1 = 0 #왼쪽위 기준점이 'W'일 경우의 최소값을 구하기위한 변수
            chk2 = 0 #왼쪽위 기준점이 'B'일 경우의 최소값을 구하기위한 변수 
            if m-j>=8:
                no = 0 #기준점을 기준으로 8x8 체스판의 몇번째 칸인지 확인하기위한 변수
                for n1 in range(i,i+8):
                    for n2 in range(j,j+8):
                        if no%2==0:
                            if board[n1][n2] != 'W':  
                                chk1+=1
                            if board[n1][n2] != 'B': 
                                chk2+=1
                        else:
                            if board[n1][n2] != 'B':
                                chk1+=1
                            if board[n1][n2] != 'W':
                                chk2+=1
                        no+=1 #다음 행으로 넘어가게되면 wb의 순서가 bw로 되므로 +1을 해준다.
                    no+=1   
                # 최솟값 구하기
                cnt = min(cnt,chk1,chk2)
print(cnt)



