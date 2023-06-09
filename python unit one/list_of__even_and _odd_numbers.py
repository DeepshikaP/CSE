odd=[]
even=[]
n=int(input("enter nth term"))
for i in range (0,n):
    a=int(input("enter a number"))
    if(a%2==0):
        even.append(a)
    else:
        odd.append(a)
print("odd list : ",odd)
print("even list : ",even)