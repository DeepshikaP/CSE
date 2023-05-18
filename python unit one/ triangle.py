a=int(input("enter the length of first side"))
b=int(input("enter the length of second side"))
c=int(input("enter the length of therd side"))
if(a+b>c and b+c>a and c+a>b):
    print("triangle can be formed")
else:
    print("triangle can't be formed")