import sys
a=[]
for i in range(1,3):
	a.append(int(sys.argv[i]))
m,n=a[0],a[1]
with open('result.txt','w') as fp:
	if m<1 or n<1 :
		fp.write('I')
	else :
		if m>=n :
			a,b=m,n
		else :
			a,b=n,m
		while b>0 :
			c=a%b
			a,b=b,c
		fp.write(str(a)+' '+str(int(m*n/a)))