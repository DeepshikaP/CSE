def seq(n):
    s=0
    t=0
    for i in range (1,n+1):
        t=t+15
        s=s+t
    return(s)
        
n=int(input("enter nth term : "))
print(seq(n))