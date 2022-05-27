import sys
x=sys.argv[1][0]
t=len(sys.argv[2])
with open('result.txt','w') as fp:
	for i in range(t):
		if sys.argv[2][i].isdigit():
			fp.write(x+sys.argv[2][i])
		else :
			fp.write(sys.argv[2][i])