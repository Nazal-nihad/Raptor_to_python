class three_d_shapes(): #base class
    def printVolume(self):
        print("The volume of the shape is ",self.volume)
    def prinArea(self):
        print("The Area of the shape is ",self.area)

class cylinders(three_d_shapes):  #derived class
    def __init__(self,r,h): #initialising values
        self.r = r
        self.h = h

    def area(self):
        self.area = round(2*3.14*self.r*(self.r+self.h),2)
    def volume(self):
        self.volume = round(3.14*self.r*self.r*self.h,2)

class sphere(three_d_shapes): #derived class
    def __init__(self,r): 
        self.r = r
    def area(self):
        self.area = round(4*3.14*self.r*self.r,2)
    def volume(self):
        self.volume = round((4/3)*3.14*self.r*self.r*self.r,2)

#cylinders operation
print("\n===== Cylinder operation =====\n")
cylinder1 = cylinders(int(input("Enter radius of cylinder : ")),int(input("Enter height of the cylinder : ")))
cylinder1.area()
cylinder1.volume()
cylinder1.prinArea()
cylinder1.printVolume()

#sphere operation
print("\n===== Sphere operation =====\n")
sphere1 = sphere(int(input("Enter the radius of the sphere : ")))
sphere1.area()
sphere1.volume()
sphere1.prinArea()
sphere1.printVolume()

