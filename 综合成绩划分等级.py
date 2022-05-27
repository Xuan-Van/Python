import sys
a,f,x=[],1,0
for i in range(1,4):
	a.append(int(sys.argv[i]))
for i in range(3):
	if a[i]<0 or a[i]>100 :
		f=0
	x+=a[i]
n=x/3
with open('result.txt','w') as fp:
	if f :
	    if n>=80 :
		    if a[0]>=90 or a[1]>=90 or a[2]>=90 :
			    fp.write('A')
	    elif a[0]>=75 and a[1]>=75 and a[2]>=75 :
		    fp.write('B')
	    elif n>=60 :
		    if a[0]>=60 and a[1]>=60 or a[0]>=60 and a[2]>=60 or a[1]>=60 and a[2]>=60 :
			    fp.write('C')
	    else :
		    fp.write('D')
	else :
		fp.write('I')