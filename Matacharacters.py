import re
from typing import Pattern

str_1 = "this is a test \r 123 "
str_2 = r"this is a test \r 123 "

print(str_1)
print(str_2)
#--------------------------------

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("1")
if re.match(pattern, "gray"):
    print("2")
if re.match(pattern, "hbfgdgray"):
    print("3")
