# age = int(input("enter yoyur age:-67 " ))
# print(age)
# if age >= 18:
#     print("you are eligble for voting ")
# else:
#     print("you are not eligle for voting")        



# nested else if
age = int(input("enter yoyur age:-" ))
gender = str(input("enter your gender:-"))

if age >= 60:
    if gender =="MALE" or gender == "male":
        print("you are an male senior cetizen")
    else:
        print("you are an female senior cetizen")
else:
    print("you are not a senoior cetizen")
    
    