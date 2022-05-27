import sys
h=int(sys.argv[1])
n=int(sys.argv[2])
a,x=[],h
a.append(h)
a.append(0.5*h)
for i in range(1,n):
	a.append(0.5*a[i])
	x+=a[i-1]
with open('result.txt','w') as fp:
	x=round(x,2)
	y=round(a[n],2)
	fp.write(str(x)+' '+str(y))