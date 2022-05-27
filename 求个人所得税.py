import sys
def shui(x):
	if x<0 :
		return -1
	else :
		n=x-1600
		if n<=0 :
			return 0
		elif n<=500 :
			return n*0.05
		elif n<=2000 :
			return (n-500)*0.1+25
		elif n<=5000 :
			return (n-2000)*0.15+25+150
		elif n<=10000 :
			return (n-5000)*0.2+25+150+450
		else :
			return (n-10000)*0.3+25+150+450+1000
with open('result.txt','w') as fp:
	n=shui(int(sys.argv[1]))
	if n==-1 :
		fp.write('I')
	else :
		fp.write('%.2f' %n)