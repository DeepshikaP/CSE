l=[]
n=1
while(n!=0):
    n=int(input("enter a number : "))
    l.append(n)
l1=l[0:(len(l)-1)]
l1.sort()
print(l1)