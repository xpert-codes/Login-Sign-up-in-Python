from getpass import getpass

global secret1
global secret2

secret1 = input("Enter a secret: ")


def reg():
    print("\nSign-Up/Register!\n")
    global user
    global psw
    user = str(input("New Username: "))
    psw = str(input("New Password: "))
    # time.sleep(1)
    print("\nPassword and Username has been set successfully! continue.")


def login():
    print("\nLogin with Username and Password!\n")
    login_username = str(input("Username: "))
    login_password = str(input("Password: "))
    if(login_username != user or login_password != psw):
        print("\nUsername or password is incorrect please try again!\n")
        login()
    else:
        print("\nSuccess!")


def result():
    print("\nYou now have access to the secerts.\n")
    print("The secert is: " + str(secret1))


def run():
    reg()
    login()
    result()


run()
