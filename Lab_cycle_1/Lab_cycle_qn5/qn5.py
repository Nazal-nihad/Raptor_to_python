
def sub_strings(text):
  #function to iterate through the string and find substrings
  sub_list = []
  for i in range(len(text)+1):
    for j in range(i+1,len(text)+1):
      sliced = text[i:j]
      sub_list.append(sliced)
  return sub_list

#function to find substrings from the string and print
def find_substrings(text):
  sub_list = sub_strings((text))
  #list is sorted and made into set to remove repetetion
  for i in sorted(set(sub_list)):
    print(i)

#function to find substrings with specified length
def k_sub(length,text):
  sub_list = sub_strings((text))
  for i in sub_list:
    if len(i)==length:
      print(i)

#function to find substrings with specified length and no of distinct characters
def n_distinct_and_k_length(distinct,length,text):
  sub_list = sub_strings((text))
  for i in sub_list:
    if len(i)==length:
      #make i to set to remove duplicate letters and check with given distinct number
      if len(set(i)) == distinct:
        print(i)

#function to find the substrings with max length and given no of distinct characters 
def n_distinct_max_k_length(distinct,text):
  sub_list = sub_strings(text)

  #finds the largest string from list and find it's length
  max_length = max(sub_list,key = len)
  check_length = len(max_length) 
  
  for i in sub_list:
    #iterate through list and check if an element matches the requirements and temporarily store it 
      if len(i) == check_length:
        if len(set(i))==distinct:
            temp = i
        #if no element matches , max length is reduced , the process is repeated until an element becomes a match
        elif check_length>len(set(i)):
          check_length -= 1

  #check if elements of original list matches the max length and the distinct character condition
  for i in sub_list:
    if len(i) == len(temp):
      if len(set(i)) == distinct:
        print(i)
#function to print palindrome substrings
def palindrome_substrings(text):
  sub_list = sub_strings(text)
  for i in sub_list:
    if i == i[::-1]: #check if reverse of word is same
      print(i)

#print all the substrings of the given string
print("\n----- To print the substrings -----")
text = str(input("Enter the word to find the substrings : "))
print("\n The substrings of ",text , " are ")
find_substrings(text)

#print substrings of the given length
print("\n----- To print the substrings with given length -----")
length = int(input(" enter the length of string to find substrings : "))
print("\n No of substrings with length ", length,)
k_sub(length,text)

#print substrings of given length and distinct characters
print("\n----- To print the substrings with given length and n distinct characters -----")
distinct = int(input(" enter the distinct number : "))
print("\n Substrings with length ",length," and ",distinct," distinct characters are : ")
n_distinct_and_k_length(distinct,length,text)

#print substrings of max length and distinct characters
print("\n----- To print the substrings of max length and given distinct characters -----")
print(" max length of substrings of the given string with ",distinct," distinct characters is : \n")
n_distinct_max_k_length(distinct,text)

#print palindrome substrings
print("\n----- To print palindrome substrings -----")
palindrome_substrings(text)