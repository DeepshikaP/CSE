l1=[]
l2=[]
n=int(input("enter nth term : "))
for i in range(0,n):
    a=input("enter a word : ")
    l1.append(a)
print(l1)
m=0
for i in l1:
    l=len(i)
    l2.append(l)
    if(len(i)>m):
        m=len(i)
        t=i
print(l2)
print("length of longest word is : ",m)
print("the word is : ",t)