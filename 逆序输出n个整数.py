import sys
i=len(sys.argv)-1
with open('result.txt','w') as fp:
	while i>=1 :
		fp.write(str(int(sys.argv[i]))+' ')
		i-=1