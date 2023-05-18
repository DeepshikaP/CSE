s=int(input("enter the lower range : "))
e=int(input("enter the upper rangr : "))
for i in range (s,e+1):
    n=0
    t=i
    while t>0 :
      a=t%10
      n=n+(a*a*a)
      t=t//10
    if(i==n):
          print(i)