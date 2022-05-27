import sys
a,b,c=0,0,0
with open('result.txt','w') as fp:
	for i in range(len(sys.argv[1])):
		x=sys.argv[1][i]
		if x.isdigit() :
			b+=1
		elif x.isalpha() :
			a+=1
		else :
			c+=1
	fp.write(str(a)+' '+str(b)+' '+str(c))