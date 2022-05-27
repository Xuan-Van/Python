import sys
a=int(sys.argv[1])
sum=0
for i in range(1,a+1):
	sum += i
with open('result.txt','w') as fp:
    if sum<1:
	    fp.write('I')
    else :fp.write(str(sum))