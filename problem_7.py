k = []
a = 2
b = 2

while (len (k) != 10001):
    if a % b != 0 :
        b = b + 1       
    elif a != b:
        a = a + 1
        b = 2
    else:
        k.append(a)
        a = a + 1
        b = 2
print (k)   
