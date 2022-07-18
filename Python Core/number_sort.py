nums = []
sort = []

while len(nums) < 3:
    num = int(input())
    nums.append(num)

while len(nums) != 0:
    x = min(nums)
    nums.remove(x)
    sort.append(x)

print(sort)