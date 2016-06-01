"""RECIPROCICAL CYCLES Problem-26"""

def max_cycle(n):
    str_n = str(1./n)
    str_n = str(10.**10/n)
    str_n = str_n.replace(".","")
    print str_n
    list_cycle = [j for i in xrange(len(str_n)) for j in range(1,(len(str_n)-i)//2+1) if str_n[i:i+j] == str_n[i+j:i+2*j]]
    if list_cycle == []:
        return 0
    else:
        return min(list_cycle)

d_max = 1000

cycles = [max_cycle(d) for d in range(1,d_max)]
print cycles
max_cycle = max(cycles)
argmax_cycle = [i+1 for i,e in enumerate(cycles) if e == max_cycle]

print argmax_cycle[0]