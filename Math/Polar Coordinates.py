import cmath
compnum = complex(input())
faza = cmath.phase(compnum)
absolute = abs(compnum)
print('{:.3f}'.format(absolute))
print('{:.3f}'.format(faza))
