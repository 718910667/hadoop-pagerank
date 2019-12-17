import sys
alpha=0.85
data=[]
for line in sys.stdin:
    fields = line.strip().split()
    k1=int(fields[0])
    k2=float(fields[1])
    k3=fields[2].split(',')
    outlinks=[int(x) for x in k3[:]]
    count=len(outlinks)
    data.append([k1,0.0])
    for x in outlinks:
        data.append([x,round(alpha*k2/count,4)])
result={}
for k,v in data:
    if k in result:
        result[k]+=v
    else:
        result[k]=v
for k,v in result.items():
    print("%d %0.4f" %(k,v+1-alpha))
