import sys
a=[]
for i in range(1,4):
	a.append(int(sys.argv[i]))
with open('result.txt','w') as fp:
    if a[0]<1 or a[1]<1 or a[2]<1 :
	    fp.write('I')
    elif (a[0]+a[1])>a[2] and (a[0]-a[1])<a[2] :
	    fp.write('Y')
    else :fp.write('N')