import sys
t,a=len(sys.argv[1]),[]
if t>10 :
	t=10
for i in range(1,t+1):
	a.append(sys.argv[1][t-i])
with open('result.txt','w') as fp:
	for i in range(t):
		fp.write(a[i])