k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 
d = 2521
i = 1
for i in range(len(k)):
    if d % k[i] != 0:
        d = d + 1
    else:
        print (d)
    
    
