mail = input("enter you mail id:-")
              


if mail.find("@") == -1 or mail.find(".") == -1:
    print("email invalid:")
else:
    print("Email valid")