import sys
x=int(sys.argv[1])
with open('result.txt','w') as fp:
	if x<0 :
		fp.write('I')
	elif x%2==0 :
		fp.write('E')
	else :
		fp.write('O')