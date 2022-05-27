import sys
x=sys.argv[1][0]
with open('result.txt','w') as fp:
	if 'a'<=x and x<='z' :
		x=x.upper()
		fp.write(x)
	elif 'A'<=x and x<='Z' :
		x=x.lower()
		fp.write(x)
	else :
		fp.write('I')