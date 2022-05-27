import sys
def factorial(x):
	if x<0:
		return x
	if x==0:
		return 1
	else :
		return x*factorial(x-1)
x=factorial(int(sys.argv[1]))
with open('result.txt','w') as fp:
	if x<0:
		fp.write('I')
	else :
		fp.write(str(x))