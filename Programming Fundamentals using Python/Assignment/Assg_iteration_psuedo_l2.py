# Pseudo code
number = int(input())
temp = number
sum = 0
while(number!=0):
    remainder = number % 10
    sum = sum + remainder^3
    number = number / 10

if (temp == sum):
    print("Armstrong number")
else:
    print("Not an armstromg number")
