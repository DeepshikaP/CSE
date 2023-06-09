l1=[]
n=int(input("enter nth term : "))
for i in range (0,n):
    a=int(input("enter element : "))
    l1.append(a)
print("list : ",l1)
for i in l1:
    if(i%2==0):
        l1.remove(i)
print("after removing even numbers : ",l1)