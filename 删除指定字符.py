import sys
a,b,t=sys.argv[1][0],[],len(sys.argv[2])
with open('result.txt','w') as fp:
	for i in range(t):
		if sys.argv[2][i]!=a :
			b.append(sys.argv[2][i])
	for i in range(len(b)):
		fp.write(b[i])