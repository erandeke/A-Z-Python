# Python Flow controls

_1)If statement_ 
syntax 
  ` if (expression) :
     //Execute the logic `
   
2)If-else statement 

syntax :
  ` if(expression):
      //Execute the logic 
   else :
     // Execute the logic `

3)if-elif-else 
syntax:
   ` if(expression):
      //Execute the logic 
    elif(expression):
      //Execute the logic
    else 
       //Execute the logic`

4)Nested if
syntax :
   `if(expression):
      if(expression):
         //Execute the logic
      else:
         //Execute  the logic 
    else:
        //Execute the logic 
`

## For Loops 

syntax:
   for i in {list}:
     //execute the logic 


## Range functions

Range functions are use to generate the sequence of numbers  

1)Creating range from 0 to 9 

print(List(range(10)));

## Combine for loop and range function to print the numbers from 0 to 9 steo by step

 for x in range(10) :
  print("Number is",x);
 
## Indexing in for loop 

`list = ['kedar','erande'];`

Here i is the index and using len function we are calculating the size of list

`for i in range(len(list)):
   print(list[i]);`


## while loop 

syntax:
  ` while (expression):
      //execute the logic `


## Break and Continue 

Break : Use for terminating from the loop when the condition is met
syntax :
`list = [1, 2, 3, 4, 5];
for x in list:
    if (x == 2):
        print(x)  # This will print 2  and next step will terminate the loop
        break;`


Continue  :It is used to skip the code for the current iteration only 

`str = "Kedar";
for x in str:
    if (x == "K"):
        continue;
    print(x);
`