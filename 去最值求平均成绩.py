import sys
a=[] 
m,f,x=int(sys.argv[1]),1,0
n=m
for i in range(1,11):
	a.append(int(sys.argv[i]))
for i in range(10):
	if a[i]<0 or a[i]>100 : f=0
	if a[i]>m : m=a[i]
	if a[i]<n : n=a[i]
	x+=a[i]
with open('result.txt','w') as fp:
	if f :
		x=x-m-n
		t=round(x/8,1)
		fp.write(str(t))
	else :
		fp.write('I')