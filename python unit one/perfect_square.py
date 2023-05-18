def ps (x):
    sq=int(x**(1/2))
    if(sq**2==x):
        print("perfect square")
    else:
        print("not a perfect square")

n=int(input("enter a number : "))
ps(n)
