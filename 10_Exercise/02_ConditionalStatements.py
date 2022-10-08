# Design student education marking system with following conditions
# if marks are lesser than 40 then mark as Fail or negative
# if marks are  in between 40 to 60 then Higher Secondary Grades
# if marks are in between 60 and 70 then first class
# if marks are beyond 70 then distinction


# List of marks :

list = [10, -1, 20, -10, 40, 60, 80];

for a in list:
    if a < 0 or a <= 40:
        print("Ohh no you are not qualified");
    elif a > 40 and a < 60:
        print("You have secured higher second grades");
    elif a >= 60 and a < 70:
        print("You have secured an first class.. congrats");
    else:
        print("Wow.. you have into distinctions!");
