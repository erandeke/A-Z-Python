# 1) Multiple 12 and 123.10 and store the result as float

# --------------------------------------------------#
var = 12 * 123.10;
print(var);
# Check the type of var
print(type(var))

# --------------------------------------------------#
# 2) Convert the above float generated result into int

num = int(var);
print(num);
print(type(num));

# --------------------------------------------------#

# 3) Create a list with following structure 1,2,3,['john','max'],1.2,1.3

list = [1, 2, 3, ['john', 'max'], 1.2, 1.3];
print(list)

# --------------------------------------------------#
# 4) Return the last and second last element of the list from #3

print(list[4:]);

# --------------------------------------------------#

# 5) Reverse the list
print(list[::-1])

# --------------------------------------------------#

# 6) Delete the second last element from the list created in # 3

del list[-2];
print(list)

# --------------------------------------------------#

# 7)create  a dictionary that includes youn name , age, education

dict = {"name:John", "age:100", "education:Msc"}
print(dict);

# --------------------------------------------------#

# 8) Remove the item name from the dictionary
# dict.pop("name");
print(dict);

# --------------------------------------------------#

# 9) Generate the upper case for the string : Hi how are you

str = "Hi how are you?";
print(str.upper());

# --------------------------------------------------#

# 10) Divide the num and return the ans with remainder

a = 2/3;
print(a);

# --------------------------------------------------#
# 11) Divide the num and return the ans without remainder

a = 2//3;
print(a);

# --------------------------------------------------#


