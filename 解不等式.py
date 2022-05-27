import sys
n=int(sys.argv[1])
x,i=1,2
with open('result.txt','w') as fp:
	if n>22 or n<1 :
		fp.write('I')
	else :
		while x<=n :
			x+=1/i
			i+=1
		fp.write(str(i-1))