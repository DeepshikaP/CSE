def seq(n,x):
    d=1
    s=0
    for i in range (1,n+1):
        d=d*2
        s=s+(x/d)
        return(s)
        
n=int(input("enter nth term : "))
x=int(input("enter x value : "))
print(seq(n,x))