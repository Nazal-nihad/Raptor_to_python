#string_int = '1 2 2 4 4 6 7 8 9 10 11'
string_int = str(input("Enter numbers with spaces "))
string_split = string_int.split()
print("=== Splitted string ===")
print(string_split)
string_to_int = [int(i) for i in string_split]
print("=== String to int is ===")
print(string_to_int)

ask = int(input("How many times you wanna roate : "))
rotate = (string_to_int[-ask:])
left = (string_to_int[0:len(string_to_int)-ask])
rotated_list = rotate+left
print("rotated ",ask," times ")
print(rotated_list)

print("== list to tuple ==")
tupled_list = tuple(string_to_int)
print(tupled_list)

print("=== duplicates removed tuple ===")
rm_dupe = tuple(set(tupled_list))
print(rm_dupe)

print("=== duplicates removed tuple to list ===")
no_dupe_list = list(rm_dupe)
print(no_dupe_list)

print("=== operation of f(x)=x^2-x ===")
op_list = [i*i - i for i in string_to_int]
print(op_list)

print("=== sorted list ===")
sorted_list = sorted(set(no_dupe_list+op_list))
print(sorted_list)
     