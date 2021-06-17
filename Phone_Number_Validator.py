import re

num = r"[1,8,9][0-9]"

phone = input()
dig = len(phone)
if (dig!=8):
    print("Invalid")
    exit()

match = re.match(num, phone)

if match:
    print("Valid")
else:
    print("Invalid")