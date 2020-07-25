k = []
a = 2
n = 600851475143 
while n > 1:
    while n %a== 0:
        k.append(a)
        n = n / a
    a = a + 1
print (k)
c = max (k)
print (c)
