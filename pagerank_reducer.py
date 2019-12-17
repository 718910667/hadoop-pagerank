import sys
import os
result={}
for line in sys.stdin:
    fields=line.strip().split()
    k=int(fields[0])
    v=float(fields[1])
    result[k]=v

file=open("process2.txt",'r')
for line in file:
    fields=line.strip().split()
    k1=int(fields[0])
    k2=round(float(fields[1]),4)
    k3=fields[2]
    if k1 in result:
        k2=result[k1]
    print("%d %0.4f %s"%(k1,k2,k3))
file.close()