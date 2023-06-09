l1=[5,9,8,3,5]
l2=[]
for i in l1 :
    f=1
    for j in range (1,i+1):
        f=f*j
    l2.append(f)
        
print("factorial of the list : ",l2)