import sys
import math
def ff(x):
	a=math.sqrt(x)
	k=2
	if x<2 :
		return -1
	else :
		while k<a:
			if x%k==0 :
				return 0
			k+=1
		return 1
x=ff(int(sys.argv[1]))
with open('result.txt','w') as fp:
	if x==-1 :
		fp.write('I')
	elif x==0 :
		fp.write('N')
	elif x==1 :
		fp.write('Y')