import random
class Box:
  def __init__(self , *numbers): #numbers - 0 = lenght , 1 = breadth , 2 = height
    if(numbers[0]==numbers[1]==numbers[2]):
      self.length = numbers[0]
      self.breadth = numbers[1]
      self.height = numbers[2]  
    else:
      if(numbers[0]==numbers[1]):
        self.length=numbers[0]
        self.breadth=numbers[1]
        self.height=numbers[2]
      elif(numbers[1]==numbers[2]):
        self.length=numbers[1]
        self.breadth=numbers[2]
        self.height=numbers[0]
      elif(numbers[2]==numbers[0]):
        self.length=numbers[0]
        self.breadth=numbers[2]
        self.height=numbers[1]
      else:
        self.length = numbers[0]
        self.breadth = numbers[1]
        self.height = numbers[2]


  def area(self):
    self.area = self.length*self.breadth
    return self.area
    
  def vol(self):
    self.vol = self.length*self.breadth*self.height
    return self.vol

bx = Box(5)
print(bx.area())
# bx = [Box(random.randint(1,100),random.randint(1,100),random.randint(1,100)) for i in range(10)]
# # bx1 = Box(random.randint(1,100),random.randint(1,100),random.randint(1,100))
# # bx2 = Box(random.randint(1,100))
# area_box = [i.area() for i in bx]
# vol_box = [i.vol() for i in bx]
# ratio_box = [round(y/x,2) for x,y in zip(area_box,vol_box)]
# # print(area_box)
# # print(vol_box)
# ind = ratio_box.index(max(ratio_box))
# print("max ratio b/w are and vol of the given boxes are ",max(ratio_box))
# print("\n The details of the box are \n")
# print("area ", area_box[ind])
# print("vol ",vol_box[ind])
# print(" dimensions \n","length ",bx[ind].length,", breadth" ,bx[ind].breadth,", height ",bx[ind].height)
# # print(bx.area())
# # print(bx.vol())