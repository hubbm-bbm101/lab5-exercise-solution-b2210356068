#exercise2
def email_check(email) :
    for letter in email :
        if "@" and "." in email :
            return True
        else :
            return False
email=input("enter your email ")
print("This email is  " , email_check(email)) 