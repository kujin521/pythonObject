s='abca*a*adef.a*b*c'
s1=s.split('.')[0]
print(s1.count('a'),s1.count('*'),sep=',',end='')