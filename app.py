import random
import string
pw_length = input("Password length : ")
while not pw_length.isdigit():
    print("Need a number to generate your password 🙃")
    pw_length = input("Password length : ")
password = "".join(random.sample(string.ascii_letters + string.digits, int(pw_length)))
print(f"Your password : {password}")