#convert integer to text
from num2words import num2words
a = int(input("Enter starting value: "))
b = int(input("\nEnter ending value: "))

print("\nstarting value is: ",a, "ending value is: ",b)
for i in range(a,b+1):
    if 1 <= i <= 9:
        print(num2words(i))
    elif i > 9 and i > 0 and i % 2 == 0:
        print(i,"is even")
    elif i > 1:
        print(i,"is odd")