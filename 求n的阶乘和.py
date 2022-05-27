import sys
def fact(x):
	if x<0 :
		return x
	if x==0 :
		return 1
	else :
		return x*fact(x-1)
n=int(sys.argv[1])
x=0
with open('result.txt','w') as fp:
	if n<2 or n>10 :
		fp.write('I')
	else :
		for i in range(1,n+1):
			x+=fact(i)
		fp.write(str(x))