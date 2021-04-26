# use infinite loop and break statement
# while True:
#     print('Please Enter Your Name: ')
#     name = input()
#     if name == 'Nahid':
#         print('ThankYou')
#         break

# use of conitue statement
# while True:
#     print('Who are you? ')
#     name = input()
#     if name !='Nahid':
#         continue
#     print('Hello There '+name+'. What is Password?')
#     password = input()
#     if password == 'Nahid':
#         break
# print('Thankyou')

# Series
# sum = 0
# for i in range(1,5):
#     sum = sum + i
#
# print(sum)
# Series = 1^2+2^2+3^2+4^2
# sum = 0
# for i in range(1,5):
#     sum = sum+i*i
#
# print(sum)

#serics 1+3+5+9
# odd_sum = 0
# for i in range(1,10,2):
#     odd_sum = odd_sum+i
#
# print(odd_sum)


#Enven
# even_sum = 0
# for i in range(2,10,2):
#     even_sum = even_sum+i
#
# print(even_sum)

# complex series = 1+(1+2)+(1+2+3)+(1+2+3+4)
sum = 0
for i in range(1,5):
    for j in range(1,i+1):
        sum = sum+j

print(sum)



