# Sum of Consecutive Numbers

n = int(input())

sum = 0
for num in range(1, n+1):
    sum += num

print(sum)