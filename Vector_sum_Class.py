class Vector2D_1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(a, b):
        return Vector2D(a.x + b.x, a.y + b.y)
    def __asd__(a,b):
        return Vector2D(a.x - b.x, a.x - b.y)


first = Vector2D(5,6)
second = Vector2D_1(2, 5)
result = Vector2D(first.x + second.x, first.y + second.y)
result1 = first + second
result2 = first.__asd__(second)


print(result.x)
print(result.y)
print("-"*20)
print(result1.x)
print(result1.y)
print(20*"-")
print(result2.x)
print(result2.y)