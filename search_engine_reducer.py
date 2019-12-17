import sys
file=open("result.txt",'r')
data=[] #URL
data1=[]#PR
for line in sys.stdin:
    fields=line.strip().split('\t')
    data.append((int(fields[0]),fields[1]))
data=sorted(data,key=lambda x:x[0],reverse=False)

for line in file:
    fields=line.strip().split()
    data1.append(fields[0])
count=0
for v,k in data:
    print(data1[count]+"\t"+k)
    count+=1
  