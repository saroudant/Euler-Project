"""COIN SUMS Problem-31
I am quite ashame of this solution ; I tried to implement
tree-based solutions but none of them was as efficient as this one."""

possible_cases = 0

for i1 in range(0,2):
    for i2 in range(0,3-2*i1):
        for i3 in range(0,(200-200*i1-100*i2)//50+1):
            for i4 in range(0,(200-200*i1-100*i2-50*i3)//20+1):
                for i5 in range(0,(200-200*i1-100*i2-50*i3-20*i4)//10+1):
                    for i6 in range(0,(200-200*i1-100*i2-50*i3-20*i4-10*i5)//5+1):
                        for i7 in range(0,(200-200*i1-100*i2-50*i3-20*i4-10*i5-5*i6)//2+1):
                            possible_cases += 1

print possible_cases


