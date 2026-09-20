#check odd and even number

n = int (input("Enter a number: "))

if n >= 1 and n % 2 == 0:
    print("Even")

elif n >= 1 and n % 2 != 0:
    print("Odd")
else:
    print("Undefined")