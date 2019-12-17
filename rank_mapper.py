import sys
data=[]
for line in sys.stdin:
    fields = line.strip().split()
    k1=int(fields[0])
    k2=float(fields[1])
    data.append((k2,k1))
data=sorted(data,key=lambda x:x[0],reverse=True)
for k,v in data:
    print("%0.2f %d" %(k,v))
    
