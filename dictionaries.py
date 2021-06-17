nums = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    None: "AJGHLKA",
}

print(nums)

print(nums[1])
print("\n")
print(1 in nums)
print(4 not in nums)
print("two" in nums)

print("\n")

print(nums.get(5, "test"))

nums[1] = "er"
print(nums[1])



