k=[]
n=1
while(n<1000):
    if n%3==0 or n%5==0:
        k.append(n)
    n=n+1
a = sum (k)
print(a)

