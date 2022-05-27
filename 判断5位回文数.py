import sys
with open('result.txt','w') as fp:
	if sys.argv[1][0]==sys.argv[1][4] and sys.argv[1][1]==sys.argv[1][3] :
		fp.write('Y')
	else :
		fp.write('N')