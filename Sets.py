nums = {1,2,3,4,5,6}

print(nums)
def test(x):
    for i in range(int(x)):
        nums.pop()
        print(nums)

test(input())