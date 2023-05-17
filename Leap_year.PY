y=int(input("enter a year : "))
if(y%400==0 or y%4==0):
    print("it is leap year ")
elif(y%100!=0):
    print("it is not a leap year")
else:
    print("it is not a leap year")