import sys
a=int(sys.argv[1])
with open('result.txt','w') as fp:
    if a<7 :fp.write('I')
    else:
        for i in range(1,a+1):
	        if i//10==7 or i%7==0 or i%10==7 :
	            pass
	        else: 
	    	    fp.write(str(i)+'\n')
