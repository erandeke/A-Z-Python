# union : Return the elements from all the sets

set1 = {1, 2, 3};
set2 = {2, 6};
set3 = {7, 2};

print(set1 | set2 | set3);  # {1, 2, 3, 6, 7}

# using union func

set4 = set1.union(set2).union(set3);
print(set4);  ## {1, 2, 3, 6, 7}

# Iersection of A and B is a set of elements that are common in both the sets.

A_set = {1, 2, 3};
B_set = {7, 1};

C_set = A_set.intersection(B_set);
print("Intersection set", C_set);  # 1

# Intersection can also be achieved by using & operator

C_set = A_set & B_set;
print(C_set);  # 1

# Difference : Difference of elements that is only in SetA but not in setB

Set_A = {1, 2, 3, 4, 5};
Set_B = {1, 4, 5, 6, 7};
print(Set_A - Set_B);  # 2,3

# Disjoint - This will return true if setA and setB does not have anything in common

setA = {1, 2};
setB = {8, 7};
print(setA.isdisjoint(setB));  # True

# symmertric difference : The set of elements which are uncommon in setA and SetB

setA = {1, 2, 3};
setB = {1, 2, 5};
print(setA.symmetric_difference(setB));  # 3,5
