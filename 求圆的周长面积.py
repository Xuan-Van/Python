import sys
pi=3.1415926
def fa(x):
	return 2*x*pi
def fb(x):
	return pi*x*x
x=int(sys.argv[1])
with open('result.txt','w') as fp:
	if x<0 :
		fp.write('I')
	else :
		fp.write(str(round(fa(x),2))+' '+str(round(fb(x),2)))