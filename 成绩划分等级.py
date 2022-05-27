import sys
x=int(sys.argv[1])
with open('result.txt','w') as fp:
	if 95<=x and x<=100 :
		fp.write('A')
	elif 85<=x and x<95 :
		fp.write('B')
	elif 70<=x and x<85 :
		fp.write('C')
	elif 60<=x and x<70 :
		fp.write('D')
	elif 0<=x and x<60 :
		fp.write('E')
	else :
		fp.write('I')