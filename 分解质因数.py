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
x=int(sys.argv[1])
y=x//2
with open('result.txt','w') as fp:
	if x<2 :
		fp.write('I')
	elif ff(x) :
		fp.write(str(x))
	else :
		for i in range(2,y):
			while x%i==0 :
				fp.write(str(i)+' ')
				x//=i