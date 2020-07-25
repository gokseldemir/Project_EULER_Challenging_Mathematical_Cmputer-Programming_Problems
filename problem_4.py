for a in range (900,999):
    for b in range (900,999):
        c = a * b
        n = c
        rev = 0
        while (n > 0):
            rev = n % 10 + rev * 10
            n = n / 10
            if(n == rev):
                print("asd")
                print(c)
        
      


    
    




