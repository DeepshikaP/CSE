y=int(input("enter no.of years : "))
s=int(input("enter the salary : "))
if(y>10):
    b=s*(10/100)
elif(y>6 and y<=10):
    b=s*(8/100)
else:
    b=s*(5/100)
print("The bonuses is :",b)