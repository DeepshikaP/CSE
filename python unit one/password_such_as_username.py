s=input("enter a mailid : ")
s1=s.split('@')
s2=s1[0]
s3=s2[::-1]
print("username : ",s2)
print("password : ",s2+s3)