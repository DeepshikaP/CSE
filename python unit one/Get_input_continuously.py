e=0
o=0
n=1
while n!=-1:
    n=int(input("enter a number : "))
    if(n%2==0):
        e=e+1
    else:
        o=o+1
print("no.of odd numbers entered : ",o)
print("no.of even numbers entered : ",e)