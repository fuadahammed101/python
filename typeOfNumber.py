#positive, nagative and zero (float or integer)

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