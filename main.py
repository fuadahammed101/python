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

#------------------------------------

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

#------------------------------------
#positive, nagative and zero (float or integer)

# n = float (input("Enter a number: "))
# if n == 0:
#     print("Zero")
# elif n > 0:
#     print("Positive ",end="")
# elif n < 0:
#     print("Nagative ",end="")

# if n.is_integer():
#     print("Integer")
# else:
#     print("Float")


#------------------------------------
#divisible by 5 and 11
# n = int(input("Enter number: "))
# if n % 5 == 0 and n % 11 == 0:
#     print ("divisible by 5 and 11")
# elif n % 5 == 0:
#     print("divisible by 5 only")
# elif n % 11 == 0:
#     print("divisible by 11 only")
# else:
#     print("Not divisible by 5 and 11")

#-----------------------------------
# #Print Even and Odd Numbers (1 to 10)
n = int(input("Enter a number: "))
if n > 0 and n % 2 == 0:
    for i in range (1, n+1):
        print(i, end=" ")