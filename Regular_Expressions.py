import re

pattern = r"test"
string_test = "this is a test, i'm testing some tests"

if re.match(pattern,"testashs"):
    print(True)
else:
    print(False)


if re.search("est","testashs"):
    print(True)
else:
    print(False)

print(re.findall('test', string_test))

match = re.search("test", string_test)
if match:
    print('\n')
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

new_string = re.sub("test", "day", string_test)
print(new_string)
