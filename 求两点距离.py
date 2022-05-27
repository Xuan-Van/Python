import sys
import math
a=[]
for i in range(1,5):
	a.append(int(sys.argv[i]))
with open('result.txt','w') as fp:
	d=round(math.sqrt((a[0]-a[2])**2+(a[1]-a[3])**2),2)
	fp.write(str(d))