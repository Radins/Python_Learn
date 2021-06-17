def function(arg_1, *args, **test):
    print(arg_1)
    print(args)
    print(test)

function(1, 2,3,6,"sdh", a=5, b=3426)


a,b,*c,d = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)
print(c)
print(d)