l=[]
l1=[]
n=int(input("enter nth term : "))
for i in range(0,n):
    a=input("enter a element : ")
    l1.append(a)
print("with duplicate value : ",l1)
for i in l1:
    if(i not in l):
        l.append(i)
print("without duplicate value : ",l)