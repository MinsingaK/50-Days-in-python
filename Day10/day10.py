"""
#my solution which is not very accurate

    def hide_password():
        encryp = []
        password = input("Enter your password : ")
        for i in password:
            j = '*'
            encryp.append(j)
        print(f"The password has {len(encryp)} characters")
        return print(encryp)

    hide_password()
"""

#the correction

def hide_password():
    password = input("Enter your password : ")
    password2 = len(password) * '*'
    return f"your password is {password2}"\
     f" and it has {len(password2)} parameters."

print(hide_password())