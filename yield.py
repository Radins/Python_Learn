def test():
    a = 1
    while a<500:
        yield a
        a += a
      
a = list(test())
print(a)

for i in test():
    print(i)

