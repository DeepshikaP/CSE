n=input("enter name of the customer")
a=int(input("emter age of customer"))
g=input("enter gender M:male ; F: femail")
p=int(input("enter the principal amount"))
t=int(input("enter no of years"))

    
def interest_calculation(p,t,r):
    i=(p*t*r)/100
    return i

if(a>60):
    r=12
    print(interest_calculation(p,t,r))
elif(a<60 and g=='F'):
    r=10
    print(interest_calculation(p,t,r))
elif(a<60 and g=='M'):
    r=9
    print(interest_calculation(p,t,r))
else:
    print("invalied")

