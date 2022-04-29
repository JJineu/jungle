# Z/재귀함수
# 
# N, r, c = map(int, input().split())

# ans = 0

# while N != 0:
# 	N -= 1

# 	# 1사분면
# 	if r < 2 ** N and c < 2 ** N:
# 		ans += ( 2 ** N ) * ( 2 ** N ) * 0

# 	# 2사분면
# 	elif r < 2 ** N and c >= 2 ** N: 
# 		ans += ( 2 ** N ) * ( 2 ** N ) * 1
# 		c -= ( 2 ** N )
        
# 	# 3사분면    
# 	elif r >= 2 ** N and c < 2 ** N: 
# 		ans += ( 2 ** N ) * ( 2 ** N ) * 2
# 		r -= ( 2 ** N )
        
# 	# 4사분면    
# 	else:
# 		ans += ( 2 ** N ) * ( 2 ** N ) * 3
# 		r -= ( 2 ** N )
# 		c -= ( 2 ** N )
    
# print(ans)



#다시
n, r, c = map(int, input().split())

z = 0
while n:
	n -= 1
	k = 2**n
	#1
	if r < k and c < k:
		z += 0
	#2
	elif r < k and c >= k:
		z += 1*(k*k)	
		c -= k
	#3
	elif r >= k and c < k:
		z += 2*(k*k)
		r -= k
	#4
	else:
		z += 3*(k*k)
		r -= k
		c -= k

print(z)


#2
index =0 
def z(n,r,c):
    global index
    if n == 1:
        if r == 0:
            index += c
        else:
            index += c+2
        return

    a = 2**(n-1)
    #1
    if r<a and c<a:
        z(n-1, r,c)
    #2
    elif r<a and c>=a:
        index += a*a
        z(n-1, r,c-a)
    #3
    elif r>=a and c<a:
        index += 2*a*a    
        z(n-1, r-a,c)
    #4
    else:
        index += 3*a*a    
        z(n-1, r-a,c-a)
        
n,r,c = map(int, input().split())
z(n,r,c)
print(index)


