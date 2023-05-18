name=input("Enter your name : ")
age=int(input("Enter your age"))
gender=input("enter your gender 'M OR F' :")
d=int(input("Enter no.of days"))
if(age>=18 and age<30 and gender == 'M' ):
    w=700*d
elif(age >=18 and age <30 and gender == 'F'):
    w=750*d
elif(age >=30 and age <=40 and gender == 'M'):
    w=800*d
elif(age>= 30 and age <= 40 and gender == 'F'):
    w=800*d
print("The wage is : ",w)