# #print the weirdness of a number based on the given conditions
# print("Enter a number: ")
# n = int(input())

# if n % 2 != 0:
#     print("Weird")
# elif n % 2 == 0 and 2 <= n <=5:
#     print("Not Weird")
# elif n % 2 == 0 and 6<=n <=20:
#     print("Weird")
# elif n % 2 ==0 and n> 20:
#     print("Not Weird")
# else:
#     print("Invalid input")    

#------------------------------------------

# #check odd and even number

# n = int (input("Enter a number: "))

# if n >= 1 and n % 2 == 0:
#     print("Even")

# elif n >= 1 and n % 2 != 0:
#     print("Odd")
# else:
#     print("Undefined")

################################################

#leap year
# def is_leap(year):
#    if (year % 400 == 0):
#        return True
#    elif (year % 100 == 0):
#           return False
#    elif (year % 4 == 0):
#        return True 
#    else:
#     return False
# year = int(input())
# print(is_leap(year))

#positive, nagative and zero

n = float (input("Enter a number: "))
if n == 0:
    print("Zero")
elif n > 0:
    print("Positive ",end="")
elif n < 0:
    print("Nagative ",end="")

if n.is_integer():
    print("Integer")
else:
    print("Float")
