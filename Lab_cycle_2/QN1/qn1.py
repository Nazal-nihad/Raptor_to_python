
ask = int(input("enter the no of months to find : "))
if ask==1:
  print(2)
else:  
  month1 = 2
  month2 = 2
  total,i=0,0
  rabbits = [2,2]
  for i in range(ask-2):
    total = month2+month1
    rabbits.append(total)
    month1 = month2
    month2 = total
    i+=1

  count=0
  for k in rabbits:
    print("Month ",rabbits.index(k)+1," : ",k)
    if k==2:
      count+=1
    if count>0:
      rabbits[rabbits.index(k)]=-1