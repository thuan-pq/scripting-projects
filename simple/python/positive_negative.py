import sys

print("Enter a number:")
num = int(input())

if (num > 0):
    print(num, " is positive")
elif (num < 0):
    print(num, " is negative")
else:
    print(num, " is zero")