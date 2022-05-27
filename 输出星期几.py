import sys
x=int(sys.argv[1])
with open('result.txt','w') as fp:
	if x==0 :
		fp.write('S')
	elif x==1 :
		fp.write('M')
	elif x==2 :
		fp.write('T')
	elif x==3 :
		fp.write('W')
	elif x==4 :
		fp.write('T')
	elif x==5 :
		fp.write('F')
	elif x==6 :
		fp.write('S')
	else :
		fp.write('I')