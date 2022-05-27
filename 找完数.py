import sys
t,s=int(sys.argv[1]),0
with open('result.txt','w') as fp:
	for i in range(1,t+1):
		for j in range(1,i):
			if i%j==0 :
				s+=j
		if s==i :
			fp.write(str(i)+' ')
		s=0