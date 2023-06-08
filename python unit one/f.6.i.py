def sequence(n):
    d=1
    s=0
    for i in range(1,n+1):
            d=d*i
            s=s+(i/d)
    return (s)
    
n=int(input("enter nth value : "))
print(sequence(n))
