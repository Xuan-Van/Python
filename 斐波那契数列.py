import sys
def fib(x):
	if x<1 or x>45 :
		return -1
	elif x==1 or x==2 :
		return 1
	else :
		return fib(x-1)+fib(x-2)
x=int(sys.argv[1])
y=fib(x)
with open('result.txt','w') as fp:
	if y==-1 :
		fp.write('I')
	else :
		fp.write(str(y))