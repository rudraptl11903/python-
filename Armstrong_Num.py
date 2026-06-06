#  Program to check Armstrong number

num = int(input("Enter a number: "))

order = len(str(num))

sum = 0
temp = num

# Calculate sum of digits raised to power
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

# Check Armstrong condition
if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
