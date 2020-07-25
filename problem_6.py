k = []

a = 3



for i in range (2,a):
    while (len (k) != 6):
        if (a %i != 0):
            k.append(a) 
        else:
            break
        a = a + 1
print (k)   
