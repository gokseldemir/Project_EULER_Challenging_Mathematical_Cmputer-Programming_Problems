k = []
a = 0
b = 1
c = a + b
while (c<4000000):
    print (c)
    if c %2== 0:
        k.append (c)
    c = a + b
    a = b
    b = c
print (k)
d = sum (k)
print (d)

    


