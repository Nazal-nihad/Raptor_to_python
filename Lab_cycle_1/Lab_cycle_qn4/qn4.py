#happy number problem 

#check if the number is happy
def happy(num):
  for i in range(1,101):
    sum = 0
    while num>0:
      remainder = num%10
      sum = sum + remainder**2
      num = num//10
#iterate 100 times if sum still not 0 returns false
    if sum==1:
      return True
    elif num<1:
      num = sum
    if i==100 :
      return False

#function to print happy numbers in the given range
def range_happy(lower , upper):
  happy_count = 0 
  for i in range(lower , upper):
    if happy(i) == True:
      happy_count += 1
      print(i)
  if happy_count == 0:
      print("there are no happy numbers in the given range")

#function to print n happy numbers
def n_happy(limit):
  n = 0
  i=1
  while i>=1:
    if happy(i) == True:
      print(i)
      n+=1
    i+=1
    if n == limit:
      break

print("\n--- To check if a number is happy or sad ---")
num = int(input("enter num : "))

#check if happy number function is true or not
if happy(num) == True:
  print(num , " is a happy number")  
else:
  print(num , " is a sad number ")
print("\n--- To find the happy numbers in the given range ---")

lower = int(input("Enter the lower limit : "))
upper = int(input("Enter the upper limit : "))
range_happy(lower,upper)

print("\n--- To find n happy numbers ---")
limit =  int(input("enter the limit : "))
n_happy(limit)
