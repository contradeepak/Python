user_name = "Deepak"
pwd = 12345

uname = input("Enter the user name:\t")
upwd = eval(input("Enter the password:\t"))

if user_name == uname and pwd == upwd:
    print("Login Successfull!")
elif user_name == uname or pwd == upwd:
    if user_name == uname and pwd != upwd:
        print("Please enter the correct password")
    elif user_name != uname and pwd == upwd:
        print("Please enter the correct username")
    else:
        print("Please enter the valid password and username")
    


