r=int(input("enter radius"))
h=int(input("enter height"))
def volume(r,h):
    volume=22/7*r*r*h
    return volume
def surface_area (r,h):
    surface_area=((2*3.14)*(r*h))+((3.14*r**2)*2)
    return surface_area
print(volume(r,h))
print(surface_area(r,h))