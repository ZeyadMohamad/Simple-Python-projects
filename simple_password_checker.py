def main():

    userpass = input("enter password:")
    resultpass = lenpass(userpass)
    print(resultpass)

def lenpass(password):

    while   True:

        if len(password) < 8: password = input("password have more than 8 characters:" )

        elif ("@" in password) or ("#" in password) or ("$"  in password) or ("_"  in password) : pass

        else: password = input("password should contain any of the following characters\"@$_#\" : ")

        if any(char.isdigit() for char in password) == False: password = input("password must have number: ")

        else: break

    return password
        
main()

# This code needs to be updated.

