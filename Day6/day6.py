# split() method allows us to separate a string in list without the parameter passed in the method

def user_name():
    mail = input("Enter your email address : ")
    username = mail.split('@')[0]
    print(f"The username is : {username.capitalize()}")
user_name()