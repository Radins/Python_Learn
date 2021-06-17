import re

pattern = r"[A-Hf-y][1-6]"

if re.search(pattern, "Yagh6"):
    print("1")
if re.search(pattern, "gahsjkgl as43"):
    print("2")

#---------------------------------

x = r".gg(spam)*"
y = r"g?"

if re.match(x, "egg"):
    print("A")
if re.match(x, "ggspamegg"):
    print("B")
if re.match(y, "ggggggggggg"):
    print("C1")

a = r"a(bc)(de)(f(g)h)i"

match = re.match(a, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())

#---------------------

asdf = r"\b(asd)\b"

match = re.search(asdf, "eu asd não sei")

if match:
    print("dsfhbkl")
