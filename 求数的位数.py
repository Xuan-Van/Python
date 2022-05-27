import sys
def ws(x):
	t=0
	if x<1 :
		return -1
	else :
		while x>0:
			x//=10
			t+=1
		return t
with open('result.txt','w') as fp:
	x=ws(int(sys.argv[1]))
	if x==-1 :
		fp.write('I')
	else :
		fp.write(str(x))