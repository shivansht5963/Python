acc_no = int(input("enter your account number:- "))
name = str(input("enter your name:- "))
gender = str(input("enter you gender:- "))

age = int(input("enter your age:-"))

balance = float(input("Enter your balance:-"))

time = int(input("enter for how many year:- "))

if age <= 60:
    if gender =="MALE" or gender == "male":
        print("OUTPUT\n")
        print("your name is ", name,"\n")
        print("you are an male")
        print("Your interest is 4%")
        interest = (balance*4*time)/100
        print("your interest is ", interest)
        print("your balance amount is :- ", balance + interest)
        
    else:
        print("OUTPUT\n")
        print("your name is ", name,"\n")
        print("you are an female ")
        print("Your interest is 5%")
        interest = (balance*5*time)/100
        print("your interest is ", interest)
        print("your balance amount is :- ", balance + interest)
else:
    print("OUTPUT\n")
    print("your name is ", name,"\n")
    print("you are a senoior cetizen")
    print("Your interest is 7%")
    interest = (balance*7*time)/100
    print("your interest is ", interest)
    print("your balance amount is :- ", balance + interest)