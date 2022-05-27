import sys
n=int(sys.argv[1])
with open('result.txt','w') as fp:
	if n<=0 :
		fp.write('I')
	elif n%400==0 or n%4==0 and n%100!=0 :
		fp.write('Y')
	else :
		fp.write('N')