
## Files in python

## Opening the file 

`f = open("filename.txt");`

## Write mode 

`f = open("filename.txt",'w');`

## Close file 

`f.close()`

## Write in file 

w is for write mode 

`with open("test.txt", "w") as f:
    f.write("Hi.. let's write to the file\n")
    f.write("Woah .. i can see some text")

## Read from the file

r is for read mode 
`f = open("test.txt","r");  
print(f.read())` # This read() will read the entire file 

if we want to read the line then readLine()  method needs to be used

## Python directory :

Python has got os modules that provides lot of utility methods  to work with directories 

`1) Make directory 
os.mkdir("test");`

`2) Rename directory
os.rename("test","new_test");`

`3) List directories 
os.listdir()`

`4) Remove directory 
os.remove("test")`