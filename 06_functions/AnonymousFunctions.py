double = lambda x: x * 2;

print(double(5));

# using filter function to filter out even elements
ob = [1, 2, 3, 4, 5, 6, 7, 8];

print(list(filter(lambda x: (x % 2 == 0), ob)));

# using map to divide each element by 2

obj = [2, 4, 6, 8, 10];

print(list(map(lambda x: (x // 2), obj)));


