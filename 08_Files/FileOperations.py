# opening the file
f = open("test.txt");

# write mode
f = open("test.txt", 'w');

# close file
f.close();

# writing in file

with open("test.txt", "w") as f:
    f.write("Hi.. let's write to the file\n")
    f.write("Woah .. i can see some text")

# reading file

f = open("test.txt", "r");
print(f.read());