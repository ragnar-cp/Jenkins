num = int(input("Enter a number: "))

# Make a copy of the original number
temp = num
rev = 0

# Reverse the number
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

# Check palindrome
if num == rev:
    print(num, "is a palindrome number.")
else:
    print(num, "is not a palindrome number.")
