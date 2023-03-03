import random
class Box:
  def __init__(self , length=1, breadth=1 , height=1):
    if(length==breadth):
        self.length=length
        self.breadth=breadth
        self.height=height
    elif(breadth==height):
      self.length=height
      self.breadth=breadth
      self.height=length
    elif(length==height):
      self.length=length
      self.breadth=height
      self.height=breadth
    else:
      self.length=length
      self.breadth=breadth
      self.height=height


  def area(self):
    self.area = self.length*self.breadth
    return self.area
    
  def vol(self):
    self.vol = self.length*self.breadth*self.height
    return self.vol
bx = [Box(random.randint(1,100),random.randint(1,100),random.randint(1,100)) for i in range(10)]
# bx1 = Box(random.randint(1,100),random.randint(1,100),random.randint(1,100))
# bx2 = Box(random.randint(1,100))
area_box = [_.area() for _ in bx]
vol_box = [_.vol() for _ in bx]
ratio_box = [round(y/x,2) for x,y in zip(area_box,vol_box)]
# print(area_box)
# print(vol_box)
ind = ratio_box.index(max(ratio_box))
print("\nMax ratio b/w are and vol of the given boxes are ",max(ratio_box))
print("\n=== The details of the box are ===")
print("Area = ", area_box[ind])
print("Volume = ",vol_box[ind])
print("\n==== dimensions ====\nlength ",bx[ind].length,", breadth" ,bx[ind].breadth,", height ",bx[ind].height,"\n================")
# print(bx.area())
# print(bx.vol())
