import random
import string

a = list(string.ascii_letters + string.digits + " !@#$%^&*")
print('\n CODED BY PRASH \n')
print("Press enter if you want to set the default value")
len = input("Password length? (default: 8) : ").strip()


def generatepass(len):
    password = []
    for i in range(int(len)):
        char = random.choice(a)
        password.append(char)
    return "".join(password)

if len == '':
    len = 8
yourpass = generatepass(len)
print("Your Generated Passcode:" ,yourpass)