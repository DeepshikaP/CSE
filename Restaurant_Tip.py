food=int(input("enter food rating from 1-5"))
service=int(input("enter service rating from 1-5"))
ambience=int(input("enter ambience rating from 1-5"))
b=int(input("enter bill amount"))
if(food==4 or food==5):
    if(service==4 or service==5 and ambience==4 or ambience==5):
        t=b*(10/100)
    else:
        t=b*(5/100)
else:
    if(service==4 or service==5 and ambience==4 or ambience==5):
        t=b*(5/100)
    else:
        t=b*(1/100)
print("The tip amount is : ",t)