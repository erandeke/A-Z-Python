# list

# list can have any data type items

list1 = ["Kedar", 10, 10.9];
print(list1)  # "Kedar", 10, 10.9

# Accessing the list elements
list1 = ['k', 0, 'e'];
print("Accessing the 1st element from the list", list1[0]);  # K

# Nested indexing
list1 = ["Kedar", [0, 1, 2, 3]];
print("nested indexing", list1[0][0]);  # K

print("nested indexing", list1[1][1]);  # 1

# Acessing the last elements : Negative indexing
list1 = ['k', 'e', 'd', 'a', 'r'];
print("Going to access the last index element", list1[-1]);  # r

# list slicing
# When we slice in python first index is inclusive but the end index is exclusive

list1 = ['k', 'e', 'd', 'a', 'r'];
print("Slice from 2nd element", list1[1:])  # edar

print("Slice from 2nd to 4th index", list1[2:4]);  # da

print("Slice from begin to end", list1[:]);  # kedar

# list Manipulation

# 1)How to change the value in list

list1 = [0, 1, 2, 3, 4];
list1[0] = 2;
print("The changed values will be printed", list1);  # 2,1,2,3,4

# 2) Append : To add an item into list
list1.append(6);
print("The appended list looks like", list1);  # 2,1,2,3,4,6

# 3)extend : If we need to add multiple elements in the list
list2 = [9, 9, 9];
list1.extend(list2);
print("Extended list", list1);  # [2, 1, 2, 3, 4, 6, 9, 9, 9]

# 4) Insert in list

list1 = [1, 3];
list1.insert(1, 4);
print("Inserted element 4 at index 1", list1)  # 1,4,3

list1[2:2] = [8, 7];
print("Inserting elements at index 2 till 2", list1);  # 1,4,8,7,3

# Deleting the elements or entire list
list1 = ['k', 'e', 'd', 'a', 'r'];

del list1[1];
print("One item is deleted from the list at index 1", list1);  # k,d,a,r

# delete the elements via slicing

del list1[1:3]
print("deleting the elements from index 1 till 3", list1);  # 'k','r';

# deleting the entire list
del list1;

# implement list as a stack (LIFO)

list1 = ['k', 'e', 'd', 'a', 'r'];
list1.pop(0);
print("Popped an element at index 0", list1)  # e,d,a,r

list1.pop(2);
print(list1)  # e ,d ,r

# Creation of list

list1 = [2 ** x for x in range(10)]
print("The list created in 2 power", list1);  # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# Copy of list
list1 = ['a', 'b'];
list2 = list1.copy();
print("The copied list we got here is ", list2);  # ['a', 'b']

# count the elements in the list
print("The func to get the size of the list", list1.count("a"));  # 1

# Sort list
list1 = [1, 4, 2, 7, 5];
list1.sort()
print("The sorted list we got here is ", list1);  # Sorted list : [1,2,4,5,7]

# More on slicing items in list

fruit = ['orange', 'mango', 'apple', 'chikku'];

# get me all fruits
print(fruit[0:4]);  # 'orange', 'mango', 'apple', 'chikku'

# get me fruits from -3 : -1 : here fruits at index -3(mango) ,-2(apple) will be included
# as by the thumb rule start index is inclusive

print(fruit[-3:-1]);  # mango , apple

# get me all fruits from -3 to : (end)
print(fruit[-3:])  # ['mango', 'apple', 'chikku']

# reverse the whole array
print(fruit[::-1]); #['chikku', 'apple', 'mango', 'orange']
