# program to terminate the loop when the condition is met

list = [1, 2, 3, 4, 5];
for x in list:
    if (x == 2):
        print(x)  # This will print 2  and next step will terminate the loop
        break;

# program to continue even if the condition is met
# Here we will print the characters in a string and escaoe the character which we dont want to print

str = "Kedar";
for x in str:
    if (x == "K"):
        continue;
    print(x);
