#구구단/반복문
n = int(input())

#공백은 print(ddfdfsfe, end=" ")
#개행은 print(1,2,3, sep='\n')
for i in range(1,10):
    print(n, '*', i, '=', n*i)


# eval() 
# 문자열 식을 인수로 받는다. 식만 처리가능, 문(=) 불가
# 
# exec()
# 문자열 문을 인수로 받는다. 여러개의 문으로 사용가능
