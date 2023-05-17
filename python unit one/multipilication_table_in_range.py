s=int(input("enter the start table"))
e=int(input("enter the end table"))
for j in range (s,e+1):
    for i in range(1,11):
        print("",j,"*",i,"=",j*i)
    print( )