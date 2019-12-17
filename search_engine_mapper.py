import sys
count=0
for line in sys.stdin:
    fields=line.strip().split()
    k1=fields[0]
    k2='tokyo'
    print(str(count)+'\t'+k1)
    count+=1
    
