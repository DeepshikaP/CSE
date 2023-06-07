def sphere(r):
    s=(4*3.14*(r**2))
    v=((4/3)*3.14*(r**3))
    print("the volume is : ",v)
    print("surface area is : ",s)

def cylinder (r,h):
    s=(2*(3.14))*(r**2)+(2*(3.14)*r*h)
    v=(3.14*(r**2)*h)
    print("the volume is : ",v)
    print("surface area is : ",s)

def cone(r,l,h):
    s=((3.14*r*l)+((3.14)*(r**2)))
    v=((1/3)*3.14*(r**2)*h)
    print("the volume is : ",v)
    print("surface area is : ",s)

def rectangular_prism(l,w,h):
    s=(2*((l*w)+(l*h)+(w*h)))
    v=l*w*h
    print("the volume is : ",v)
    print("surface area is : ",s)

def triangular(b,h,l,s1):
    s=((b*h)+(2*l*s1)+(l*b))
    v=((1/2)*(b*l)*h)
    print("the volume is : ",v)
    print("surface area is : ",s)

print("1.sphere")
print("2.cylinder")
print("3.conr")
print("4.rectangular prism")
print("5.triangular prism")

n=float(input("enter your choice"))
if(n==1):
    r=float(input("enter radius"))
    sphere(r)

elif(n==2):
    r=float(input("enter radius"))
    h=float(input("enter height"))
    cylinder (r,h)

elif(n==3):
    r=float(input("enter radius"))
    h=float(input("enter height"))
    l=float(input("enter side"))
    cone(r,l,h)

elif(n==4):
    h=float(input("enter height"))
    l=float(input("enter length"))
    w=float(input("enter width"))
    rectangular_prism(l,w,h)

elif(n==5):
    h=float(input("enter height"))
    l=float(input("enter length"))
    b=float(input("enter base"))
    s1=float(input("enter side"))
    triangular(b,h,l,s1)
    
