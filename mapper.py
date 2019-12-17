import sys
set=set()
for line in sys.stdin:
    fields = line.strip().split('\n')
    count=0
    for item in fields:
        item1,item2=item.split("\t")
        if item1 not in set:
            if set is not None:
                print("\n",end='')
            print(item1+"\t"+item2,end='')
        else:
            print(","+item2,end="")
        set.add(item1)
