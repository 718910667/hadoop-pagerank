import sys
result = {}
for line in sys.stdin:
    fields = line.strip().split('\t')
    #print(fields[-1])
    #print(type(line))   #str
    #print(type(fields)) #list
    k = fields[0]
    v = fields[-1]
    print(k+" "+"1.0"+" "+v)