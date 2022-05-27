import sys
import math
x,k,a=int(math.sqrt(len(sys.argv))),1,[]
for i in range(x):
	temp=[]
	for j in range(x):
		temp.append(int(sys.argv[k]))
		k+=1
	a.append(temp)
with open('result.txt','w') as fp:
	for i in range(x):
		for j in range(x):
			fp.write(str(a[j][i])+' ')