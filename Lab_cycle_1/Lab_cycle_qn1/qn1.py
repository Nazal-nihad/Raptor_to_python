
num = int(input("enter a 4 digit number : "))
length = len(str(num))

if(length == 4):
  i , reverse , sum = 1,0,0
  odd_place , even_place = 1,1

  while(i<=length):
    #finding the last digit
    a = num%10

    if i%2==0: 
      #checking even place , multiplying and storing                
      even_place = even_place*a 
    else:
      #checking odd place , multiplying and storing                      
      odd_place = odd_place*a 

    #reverse the integer
    reverse = reverse*10 + a
    #find sum of integer 
    sum += a 
    #change original digit                  
    num=num//10      
    i+=1

  #difference b/w product of numbers at odd and even place 
  difference =  even_place-odd_place
  print("the reverse of the number is : ",reverse )
  print(" the sum of the integers in the number is : ",sum) 
  print( " the differce b/w products of integers in even place and odd place is : ",difference)
else:
  print("Please enter a 4 digit number!!")