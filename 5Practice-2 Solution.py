# Leap-year-code
# year = int(input('Enter the year to check: '))
#
# if year % 400 == 0:
#     print('This is a leap year.')
# elif year % 100 == 0:
#     print('This is not a leap year')
# elif year % 4 == 0:
#     print('This is leap year')
# else:
#     print('This is not leap year')

# patten printing
#    *
#   ***
#  *****
# ********
# row = int(input())
#
# count = 0
# for i in range(0, row):
#     for j in range(0, row-i-1):
#         print(end=" ")
#
#     count = count+1
#     for k in range(0, i+count):
#         print("*", end= "")
#
#     print(" ")

# Patten-2
#   *
#  **
#  ***
# ****
# row = int(input())
#
# count = 0
# for i in range(0, row):
#     for j in range(0, row-i-1):
#         print(end=" ")
#
#     for k in range(0, i+1):
#         print("*",end="")
#
#     print(" ")

# To check a number is armstrong or not?
print('Enter the number: ')

digit = int(input())
temp = digit
sum = 0

while digit != 0:
    digit_mod = digit % 10
    digit = digit//10
    sum=sum + digit_mod**3


if sum == temp:
    print("This is armstrong")
else:
    print("This number is not armstrong")

