import math

#function to get input of 3 sides of a triangle
def sides():
  s1 = int(input("enter the side 1 : "))
  s2 = int(input("enter the side 2 : "))
  s3 = int(input("enter the side 3 : "))
  return s1,s2,s3

#function to find are from the given sides 
def area(s1,s2,s3):
  area = 0
  #semi perimeter 
  s = (s1+s2+s3)/2
  area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
  print("area of the triangle is : ",round(area,2)) #area rounded off to 2 digits
  return area

#function to find contribution of each triangle in total area
def percentage(area1,area2):
  total = area1+area2
  print("\n total are of the triangles are : ",round(total,2))
  #contribution of triangle 1 and round off to 2 digits
  triangle1 = round(area1*100/total,2)
  #contribution of triangle 2 and round off to 2 digits
  triangle2 = round(area2*100/total,2)

  print(" percentage contribution of triangle 1 in total area is : ",triangle1,"%")
  print(" percentage contribution of triangle 2 in total area is : ",triangle2,"%")

print("\n --- Triangle 1 ---")
#call function to get sides
a,b,c = sides()
#call function to find area
area1 = area(a,b,c)

print("\n --- Triangle 2 ---")
a1,b2,c3 = sides()
area2 = area(a1,b2,c3)

#call function to find percentage of each
percentage(area1,area2)