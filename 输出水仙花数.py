import sys
def sxh(x):
	a,b,c=x//100,x//10%10,x%10
	y=a**3+b**3+c**3
	if x==y :
		return 1
	else :
		return 0
with open('result.txt','w') as fp:
	for i in range(100,999):
		if sxh(i) :
			fp.write(str(i)+' ')